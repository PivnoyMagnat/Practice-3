from ftplib import FTP

def list_ftp_files(host, username, password):
    try:
        ftp = FTP(host)
        ftp.login(username,password)
        print("Correct!")
        print("List of files on server:")
        ftp.retrlines('LIST')
        ftp.quit()
    except Exception as e:
        print(f"Something gone wrong (as always): {e}")

if __name__ == "__main__":
    host = input("Write some FTP domain (or use Test.Rebex.Net): ")
    username = input("Write name (demo for Test.Rebex.Net): ")
    password = input("Write password (password for Test.Rebex.Net): ")
    list_ftp_files(host, username, password)