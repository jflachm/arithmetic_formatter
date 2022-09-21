    # Admissible operators
    operators = ['+', '-']

    for i,prob in enumerate(problems):

      # Error if there is non space
      if ' ' not in prob:
          return(print("Error: Must contain spaces."))
    
      separated_problem = prob.split()
      number1 = separated_problem[0]
      operator = separated_problem[1]
      number2 = separated_problem[2]
        
      # Error if there is a non admissible operator
      if operator not in operators:
          return "Error: Operator must be '+' or '-'."
        
      # Error if number doesn't only contains digits
      if number1.isdigit() == False or number2.isdigit() == False :
        return "Error: Numbers must only contain digits."
        
      # Error if number exceeds four digits
      if len(number1) > 4 or len(number2) > 4:
        return "Error: Numbers cannot be more than four digits."

      space = max(len(number1), len(number2))

      if i == 0:        
        line1 += number1.rjust(space+2)
        line2 += operator + ' ' + number2.rjust(space)
        line3 += '-' * (space+2)
        line4 += str(eval(prob)).rjust(space+2)

      else:
        line1 += ' '*4 + number1.rjust(space+2)
        line2 += ' '*4 + operator + ' ' + number2.rjust(space)
        line3 += ' '*4 + '-' * (space+2)
        line4 += ' '*4 + str(eval(prob)).rjust(space+2)

    if answer == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
