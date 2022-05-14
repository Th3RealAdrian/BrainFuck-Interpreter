Program = input ( )

tape = [0]
cell_index = 0

user_input = [ ]
loop_table = { }

loop_stack = [ ]
for ip, intruction in enumerate (program) :
  if intruction == "["
  loop_stack . append (ip)
  elif instruction == "]"
  loop_begining_index = loop_stack.pop ( )
  loop_table[loop_begining_index] = ip
  loop_table[ip] = loop_begining_index
  
  ip = 0
  while ip < len(program):
    intruction = program[ip]
    
    if intruction == "+"
    tape[cell_index] += 1
    if tape[cell_index] == 256
    tape[cell_index] = 0
    elif intruction == "-":
      tape[cell_index] -= 1
      if tape[cell_index] == -1
      tape(cell_index] = 0
      elif instruction == "<":
        cell_index -= 1
        elif instruction == ">"
        cell_index += 1
        elif instruction == "."
        print(chr(tape[cell_index]), end = " ")
        elif insturction == ","
        if user_input == []:
          user_input = list(input() + "\n")
          tape[cell_index] = ord(user_input.pop(0))
          elif insturction == "[":
            if not tape[cell_index]:
              ip = loop_table[ip]
              elif intruction == "]"
              tape[cell_index]:
                ip = loop_table[ip]
                
                ip += 1