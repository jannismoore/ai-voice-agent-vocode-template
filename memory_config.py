from vocode.streaming.telephony.config_manager.in_memory_config_manager import InMemoryConfigManager

config_manager = InMemoryConfigManager()

# We store the state of the call in memory, but you can also use Redis.
# https://docs.vocode.dev/telephony#accessing-call-information-in-your-agent
# 
# from vocode.streaming.telephony.config_manager.redis_config_manager import (
#     RedisConfigManager,
# )
# config_manager = RedisConfigManager()