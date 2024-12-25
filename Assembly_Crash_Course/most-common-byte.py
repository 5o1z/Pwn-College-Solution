'''
A function stack frame is a set of pointers and values pushed onto the stack to save things for later use and allocate space on the stack for function variables.

First, let's talk about the special register rbp, the Stack Base Pointer.

The rbp register is used to tell where our stack frame first started.
As an example, say we want to construct some list (a contiguous space of memory) that is only used in our function.
The list is 5 elements long, and each element is a dword. A list of 5 elements would already take 5 registers, so instead, we can make space on the stack!

The assembly would look like:

; setup the base of the stack as the current top
mov rbp, rsp
; move the stack 0x14 bytes (5 * 4) down
; acts as an allocation
sub rsp, 0x14
; assign list[2] = 1337
mov eax, 1337
mov [rbp-0x8], eax
; do more operations on the list ...
; restore the allocated space
mov rsp, rbp
ret

Notice how rbp is always used to restore the stack to where it originally was. If we don't restore the stack after use, we will eventually run out.
In addition, notice how we subtracted from rsp, because the stack grows down.
To make the stack have more space, we subtract the space we need. The ret and call still work the same.
'''
'''
Once again, please make function(s) that implement the following:

most_common_byte(src_addr, size):
  i = 0
  while i <= size-1:
    curr_byte = [src_addr + i]
    [stack_base - curr_byte] += 1
    i += 1

  b = 0
  max_freq = 0
  max_freq_byte = 0
  while b <= 0xff:
    if [stack_base - b] > max_freq:
      max_freq = [stack_base - b]
      max_freq_byte = b
    b += 1

  return max_freq_byte
Assumptions:

There will never be more than 0xffff of any byte
The size will never be longer than 0xffff
The list will have at least one element
Constraints:

You must put the "counting list" on the stack
You must restore the stack like in a normal function
You cannot modify the data at src_addr'''

from pwn import *

p = process('/challenge/./run')

code = asm('''
most_common_byte:

    ; Prologue: set up stack frame
    push rbp
    mov rbp, rsp
    sub rsp, 256                ; Allocate 256 bytes on the stack for the counting array

    ; Initialize counting array to zero
    xor rcx, rcx                ; Clear rcx, which will serve as a loop counter

init_count_w_zero:
    mov byte ptr [rbp + rcx - 256], 0 ; Set counting_array[rcx] to 0
    inc rcx                     ; Increment counter
    cmp rcx, 256                ; Check if rcx < 256
    jl init_count_w_zero        ; Loop until all 256 bytes are initialized

    ; Count occurrences of each byte in the input
    xor rcx, rcx                ; Reset rcx to 0

count_bytes:
    movzx eax, byte ptr [rdi + rcx]   ; Load byte from src_addr[rcx] into eax
    inc byte ptr [rbp + rax - 256]    ; Increment the corresponding count in the counting array
    inc rcx                     ; Move to the next byte in the input
    cmp rcx, rsi                ; Check if rcx < size (input length)
    jl count_bytes              ; Loop until all bytes are counted

    ; Find the byte with the highest frequency
    xor rcx, rcx                ; Reset rcx to iterate over the counting array
    xor rdx, rdx                ; Clear rdx (max frequency)
    xor rbx, rbx                ; Clear rbx (most common byte)

find:
    movzx eax, byte ptr [rbp + rcx - 256] ; Load count[rcx] into eax
    cmp al, dl                  ; Compare count with the current max frequency
    jle next_byte               ; If count <= max frequency, skip updating

update_max:
    mov dl, al                  ; Update max frequency (dl = count[rcx])
    mov bl, cl                  ; Update most common byte (bl = rcx)

next_byte:
    inc rcx                     ; Move to the next byte in the counting array
    cmp rcx, 256                ; Check if rcx < 256
    jl find                     ; Loop until all bytes are checked

    ; Return the most common byte
    mov al, bl                  ; Place the most common byte in al (return value)
    leave                       ; Restore stack and base pointer
    ret                         ; Return to the caller
''', arch='amd64', os='linux')

p.send(code)
p.interactive()


'''
Executing your code...
---------------- CODE ----------------
0x400000:    push      rbp
0x400001:    mov       rbp, rsp
0x400004:    sub       rsp, 0x100
0x40000b:    xor       rcx, rcx
0x40000e:    mov       byte ptr [rbp + rcx - 0x100], 0
0x400016:    inc       rcx
0x400019:    cmp       rcx, 0x100
0x400020:    jl        0x40000e
0x400022:    xor       rcx, rcx
0x400025:    movzx     eax, byte ptr [rdi + rcx]
0x400029:    inc       byte ptr [rbp + rax - 0x100]
0x400030:    inc       rcx
0x400033:    cmp       rcx, rsi
0x400036:    jl        0x400025
0x400038:    xor       rcx, rcx
0x40003b:    xor       rdx, rdx
0x40003e:    xor       rbx, rbx
0x400041:    movzx     eax, byte ptr [rbp + rcx - 0x100]
0x400049:    cmp       al, dl
0x40004b:    jle       0x400051
0x40004d:    mov       dl, al
0x40004f:    mov       bl, cl
0x400051:    inc       rcx
0x400054:    cmp       rcx, 0x100
0x40005b:    jl        0x400041
0x40005d:    mov       al, bl
0x40005f:    leave
0x400060:    ret'''
