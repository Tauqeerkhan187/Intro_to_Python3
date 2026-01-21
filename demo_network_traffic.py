import numpy as np
import matplotlib.pyplot as plt

def simulate_net_traffic(duration_sec=300, sample_rate=2, seeds=42):
    """Return t(time array (secs)), traffic_mbps: sim traffic (Mbps)"""
    rng = np.random.default_rng(seeds)
    
    # time axis
    n = int(duration_sec * sample_rate)
    t = np.linspace(0, duration_sec, n, endpoint = False)
    
    # baseline and periodic pattern
    baseline = 30
    wave_1 = 10 * np.sin(2 * np.pi * t / 60) # one min wave
    wave_2 = 5 * np.sin(2 * np.pi * t / 15) # 15 sec wave
    
    # rand noise
    rand_noise = rng.normal(0, 3, size=n)
    
    traffic = baseline + wave_1 + wave_2 + rand_noise
    
    # bursts(downloads, scans, spikes)
    burst_count = 8
    for _ in range(burst_count):
        start = rng.integers(0, n - 1)
        burst_len = rng.integers(int(1 * sample_rate), int(6 * sample_rate))  # 1–6 secs
        burst_amp = rng.uniform(20, 70)  # Mbps spike
        end = min(n, start + burst_len)
        traffic[start:end] += burst_amp
        
    # Clamp to 0+ Mbps
    traffic = np.clip(traffic, 0, None)
    return t, traffic

def moving_average(x, window):
    window = max(1, int(window))
    kernel = np.ones(window) / window
    return np.convolve(x, kernel, mode="same")

def main():
    
    duration = 300
    sample_rate = 2 
    
    # Simulate 5 minutes at 2 samples/second
    t, traffic = simulate_net_traffic(duration, sample_rate)

    # Smooth it (e.g., 10-second moving average)
    sample_rate_hz = sample_rate
    window = int(10 * sample_rate_hz)
    traffic_smooth = moving_average(traffic, window)

    # Plot
    plt.plot(t, traffic, label="Traffic (raw)")
    plt.plot(t, traffic_smooth, label="Traffic (10s moving avg)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Throughput (Mbps)")
    plt.title("Network Traffic Over Time (Simulated)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()