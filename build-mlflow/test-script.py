import time
from utils import Log

log = Log()
cnt = 5
i = 1
while i < cnt:
    log.logger.warning(f"tracking server ready?{cnt - i} sec(s) remaining...")
    i += 1
    time.sleep(1)