import speedtest
import sys
import time
from   termcolor import colored

def run_speedtest():
    st = speedtest.Speedtest()

    try:
        print(colored("Fetching server list...", 'yellow'))
        st.get_servers()

        print(colored("Choosing the best server...", 'yellow'))
        st.get_best_server()

        print(colored("Testing download speed...", 'yellow'))
        download_speed = st.download() / 1_000_000  # Convert to Mbps

        print(colored("Testing upload speed...", 'yellow'))
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        print(colored("Testing ping...", 'yellow'))
        ping = st.results.ping

        print(colored("\nSpeedtest Results:", 'cyan'))
        print(colored(f"Download Speed: {download_speed:.2f} Mbps", 'green'))
        print(colored(f"Upload Speed: {upload_speed:.2f} Mbps", 'green'))
        print(colored(f"Ping: {ping} ms", 'green'))
    except speedtest.SpeedtestError as e:
        print(colored(f"Speedtest error: {str(e)}", 'red'))
    except Exception as e:
        print(colored(f"An error occurred: {str(e)}", 'red'))
        sys.exit(1)

if __name__ == "__main__":
    run_speedtest()
