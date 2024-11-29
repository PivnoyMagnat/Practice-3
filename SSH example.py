import paramiko

def execute_ssh_command(host, username, password, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host,username,password)
        print(f"Do command ls or any command u write: {command}")
        stdin, stdout, stderr = client.exec_command(command)
        print("Command result:")
        print(stdout.read().decode())
        print("Errors (as always):")
        print(stderr.read().decode())
        client.close()
    except Exception as e:
        print(f"Some problem with SSH (can't help u with that): {e}")

if __name__ == "__main__":
    host = input("SSH domain?(test.rebex.net): ")
    username = input("Write username (demo): ")
    password = input("Write password (password): ")
    command = input("Write command u want, it wont work anyway: ")
    execute_ssh_command(host, username, password, command)