TX_STATUS_REVERT = -4       # EVM execution reverted
TX_STATUS_TIMEOUT = -3      # not found in chain within deadline
TX_STATUS_ERROR = -2        # protocol-level error
TX_STATUS_QUEUE_ERROR = -1  # queued but errored before execution
TX_STATUS_QUEUED = 0        # waiting in MocQueue
TX_STATUS_EXECUTED = 1      # confirmed and executed
