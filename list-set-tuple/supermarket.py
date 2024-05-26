# Tom is working at the supermarket, and he needs your help to keep track of his clients.
# Write a program that reads lines of input consisting of a customer's name and adds it to the end of a queue until
# "End" is received. If, in the meantime, you receive the command "Paid", you should print each customer in the order
# they are served (from the first to the last one) and empty the queue.

command = input()
clients = []

while command != "End":
    if command != "Paid":
        clients.append(command)
    else:
        for i in clients:
            print(i)
        clients.clear()
    command = input()

print(f"{len(clients)} people remaining.")
