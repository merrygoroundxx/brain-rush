import parallel
import time

# 初始化并口
p = parallel.Parallel()

# 并口地址（可能需要根据你的硬件配置进行调整）
p.setData(0x378)

def send_trigger(trigger_value):
    # 发送触发信号
    p.setData(trigger_value)
    # 保持信号一段时间（例如100ms）
    # time.sleep(0.1)
    # 清除信号
    # p.setData(0)
