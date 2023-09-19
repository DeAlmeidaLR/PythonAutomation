#pip install speedtest-cli

import speedtest

def perform_speed_test():
    st = speedtest.Speedtest()

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    print("Network Speed Test")
    perform_speed_test()