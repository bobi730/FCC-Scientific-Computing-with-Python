def arithmetic_arranger(problems, show_solution=False):

  # The largest ammount of problems we can process is 5
  if len(problems) > 5:
    return "Error: Too many problems."

  list_of_problems = [problem.split() for problem in problems]

  for problem in list_of_problems:
    # Check for formattig errors
    if len(problem) != 3:
      return "Error: Invalid problem format."

    # we want the numbers to only contain digits
    if (not problem[0].isdigit()) or (not problem[2].isdigit()):
      return "Error: Numbers must only contain digits."

    # we want the numbers to have at most 4 digits
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

   # we only allow operators + and -
    if problem[1] not in {'+', '-'}:
      return "Error: Operator must be '+' or '-'."

  num = len(problems)
  list_of_lengths = [
      max(len(problem[0]), len(problem[2])) for problem in list_of_problems
  ]
  list_of_solutions = [str(eval(problem)) for problem in list_of_problems]

  line_1, line_2, line_3, solution_line = "", "", "", ""

  for i in range(num):
    problem = list_of_problems[i]
    length = list_of_lengths[i]
    solution = list_of_solutions[i]

    # Construct the lines
    line_1 += "  " + " " * (length - len(problem[0])) + problem[0] + " " * 4
    line_2 += problem[1] + " " + " " * (length -
                                        len(problem[2])) + problem[2] + " " * 4
    line_3 += "--" + "-" * length + " " * 4
    solution_line += " " + " " * (length - len(solution) +
                                  1) + solution + " " * 4

  # construct final solution with final spaces removed
  arranged_problems = line_1.rstrip() + '\n' + line_2.rstrip(
  ) + '\n' + line_3.rstrip()
  if show_solution:
    arranged_problems += '\n' + solution_line.rstrip()

  return arranged_problems


def eval(problem):
  if problem[1] == '+':
    return int(problem[0]) + int(problem[2])
  else:
    return int(problem[0]) - int(problem[2])
