import os

# os.chdir("2.4.2/main")
# answer = ["main"]
# for current_dir, dirs, files in os.walk("."):
#     for file in files:
#         if file[-3:] == ".py":
#             answer.append(current_dir)
#             break
# answer.remove(".")
# answer = list(map(lambda x: x.replace("\\", "/").replace("./", "main/"), answer))

# with open("../result_2.4.2.txt", "w+") as result:
#     result.write("\n".join(answer))

print(os.getcwd)
