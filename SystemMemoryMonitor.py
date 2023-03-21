import psutil
from plyer import notification

while True:
    # Get system memory usage
    memory_usage = psutil.virtual_memory().percent
    
    # Check if memory usage exceeds 90%
    if memory_usage > 90:
        # Create notification
        notification.notify(
            title="Memory usage warning",
            message=f"Memory usage is at {memory_usage}%.",
            app_name="System Monitor",
            timeout=10
        )
        
    # Wait for 5 minutes before checking again
    time.sleep(300)
