import datetime
from collections import OrderedDict

from eth_typing import HexStr
from web3 import Web3

from .logger import log
from .status import TX_STATUS_ERROR, TX_STATUS_QUEUE_ERROR, TX_STATUS_QUEUED, TX_STATUS_EXECUTED


def sanitize_address(address):
    # not allow empty addresses
    if address == "0x0000000000000000000000000000000000000000":
        return None

    return Web3.to_checksum_address(address.replace("0x000000000000000000000000", "0x"))


def oper_id_to_int(oper_id):

    if str(oper_id).startswith("0x"):
        return Web3.to_int(hexstr=HexStr(oper_id))
    else:
        return int(oper_id)


class BaseEvent:

    name = 'Name'
    precision = 10 ** 18

    def __init__(self, options, connection_helper, contracts_loaded, contracts_addresses, filter_contracts_addresses, block_info):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.contracts_addresses = contracts_addresses
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info

    def parse_event(self, parsed_receipt, decoded_event):
        fields = dict()
        for field in decoded_event:
            fields[field['name']] = field['value']

        return dict(**parsed_receipt, **fields)



class EventMocMultiCollateralGuardMicroLiquidationExecuted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocMultiCollateralGuard_MicroLiquidationExecuted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["executor_"] = sanitize_address(parsed["executor_"])
        d_event["originBucket"] = sanitize_address(parsed["originBucket"])
        d_event["targetBucket_"] = sanitize_address(parsed["targetBucket_"])
        d_event["targetTP_"] = sanitize_address(parsed["targetTP_"])
        d_event["qACtoSwap_"] = parsed["qACtoSwap_"]
        d_event["qACOut_"] = parsed["qACOut_"]
        d_event["qTPtoRebalance_"] = parsed["qTPtoRebalance_"]
        d_event["qACExecFee_"] = parsed["qACExecFee_"]
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocMultiCollateralGuard MicroLiquidationExecuted :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocMultiCollateralGuardPartialLiquidationExecuted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocMultiCollateralGuard_PartialLiquidationExecuted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["executor_"] = sanitize_address(parsed["executor_"])
        d_event["originBucket"] = sanitize_address(parsed["originBucket"])
        d_event["targetBucket_"] = sanitize_address(parsed["targetBucket_"])
        d_event["targetTP_"] = sanitize_address(parsed["targetTP_"])
        d_event["qACtoSwap_"] = parsed["qACtoSwap_"]
        d_event["qACOut_"] = parsed["qACOut_"]
        d_event["qTPtoRebalance_"] = parsed["qTPtoRebalance_"]
        d_event["qACExecFee_"] = parsed["qACExecFee_"]
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocMultiCollateralGuard PartialLiquidationExecuted :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocMultiCollateralGuardBucketLiquidated(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocMultiCollateralGuard_BucketLiquidated')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["originBucket"] = sanitize_address(parsed["originBucket"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocMultiCollateralGuard BucketLiquidated :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocMultiCollateralGuardBucketChange(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocMultiCollateralGuard_BucketChange')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["bucketIndex_"] = parsed["bucketIndex_"]
        d_event["bucket_"] = sanitize_address(parsed["bucket_"])
        d_event["bucketParams_"] = parsed["bucketParams_"]
        d_event["mocSwappers"] = parsed["mocSwappers"]
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocMultiCollateralGuard BucketChange :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocPeggedTokenChange(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Moc_PeggedTokenChange')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["i_"] = parsed["i_"]
        d_event["tpTokenAddress_"] = sanitize_address(parsed["tpTokenAddress_"])
        d_event["peggedTokenParams_"] = str(parsed["peggedTokenParams_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Moc PeggedTokenChange :: bucket: {0} :: id: {1}".format(self.bucket_index, d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocLiqTPRedeemed(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Moc_LiqTPRedeemed')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["tp_"] = sanitize_address(parsed["tp_"])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"]).lower()
        d_event["recipient_"] = sanitize_address(parsed["recipient_"]).lower()
        d_event["qTP_"] = parsed["qTP_"]
        d_event["qAC_"] = parsed["qAC_"]
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Moc_LiqTPRedeemed :: bucket: {0} :: id: {1}".format(self.bucket_index, d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocSuccessFeeDistributed(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection SuccessFeeDistributed
        collection = self.connection_helper.mongo_collection('event_Moc_SuccessFeeDistributed')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["mocGain_"] = str(parsed["mocGain_"])
        d_event["tpGain_"] = str(parsed["tpGain_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Success Fee Distributed :: bucket: {0} :: id: {1}".format(self.bucket_index, d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocSettlementExecuted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)


    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Moc_SettlementExecuted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Settlement Executed :: bucket: {0} :: id: {1}".format(self.bucket_index, d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocTCInterestPayment(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Moc_TCInterestPayment')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["interestAmount_"] = str(parsed["interestAmount_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: TC Interest Payment :: bucket: {0} :: id: {1} ".format(self.bucket_index, d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocTPemaUpdated(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Moc_TPemaUpdated')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["i_"] = oper_id_to_int(parsed["i_"])
        d_event["oldTPema_"] = str(parsed["oldTPema_"])
        d_event["newTPema_"] = str(parsed["newTPema_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: TP Ema Updated :: bucket: {0} :: id: {1}".format(self.bucket_index, d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventMocQueueOperationError(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection OperationQueueStatus
        collection = self.connection_helper.mongo_collection('event_MocQueue_OperationError')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        # Error Code:
        # LOW_COVERAGE: 0x79121201
        # INSUFFICIENT_QAC_SENT: 0x0b63f1a7
        # INSUFFICIENT_TC_TO_REDEEM: 0xa5db715d
        # INSUFFICIENT_TP_TO_MINT: 0xc39b739f
        # INSUFFICIENT_TP_TO_REDEEM: 0x3fe8c5eb
        # INSUFFICIENT_QTP_SENT: 0xf4063b46
        # QAC_NEEDED_MUST_BE_GREATER_ZERO: 0xf3e39b5d
        # QAC_BELOW_MINIMUM: 0x54cde313
        # QTP_BELOW_MINIMUM: 0x9cb8fd64
        # QTC_BELOW_MINIMUM: 0xf577bef5
        # INVALID_FLUX_CAPACITOR_OPERATION: 0x1f69fa6a
        # TRANSFER_FAILED: 0x90b8ec18

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["bucket_index"] = self.bucket_index
        d_event["errorCode_"] = parsed["errorCode_"]
        d_event["msg_"] = parsed["msg_"]
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: OperationError :: bucket: {0} :: operId_: {1}".format(self.bucket_index, d_event["operId_"]))
        log.info(d_event)

        # change status in collection operations
        collection = self.connection_helper.mongo_collection('operations')

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = oper_id_to_int(d_event["operId_"])
        d_oper["bucket_index"] = self.bucket_index
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["errorCode_"] = d_event["errorCode_"]
        d_oper["msg_"] = d_event["msg_"]
        d_oper["status"] = TX_STATUS_QUEUE_ERROR
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        # Issue: ROC-990: Operation limited by the flux capacitor should stay in the queue and not fail
        # msg: Max flux capacitor operation reached
        # Constant: MAX_FLUX_CAPACITOR_REACHED
        # if d_oper["errorCode_"] == "0x0db483ca":
        #     # skip if is a problem with flux capacitor stay on the queue, so set queue status
        #     log.warning("Event :: OperationError :: bucket: {0} :: operId_: {1} Skipping... Fluxcapacitor limitation not failing".format(
        #         self.bucket_index, d_event["operId_"]))
        #     d_oper["status"] = 0

        operation = collection.find_one({"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]})
        if operation:
            if operation['status'] >= 1:
                # if executed don't update
                log.warning("Event :: OperationError :: bucket: {0} :: operId_: {1} Skipping writting to database is already in status 1".format(
                    self.bucket_index, d_event["operId_"]))
                return d_oper, parsed

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        return d_oper, parsed


class EventMocQueueUnhandledError(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):
        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_UnhandledError')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["bucket_index"] = self.bucket_index
        d_event["reason_"] = parsed["reason_"]
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocQueue_UnhandledError :: bucket: {0} :: operId_: {1}".format(
            self.bucket_index, d_event["operId_"]))
        log.info(d_event)

        # change status in collection operations
        collection = self.connection_helper.mongo_collection('operations')

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = oper_id_to_int(d_event["operId_"])
        d_oper["bucket_index"] = self.bucket_index
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["reason_"] = d_event["reason_"]
        d_oper["status"] = TX_STATUS_ERROR
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        operation = collection.find_one({"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]})
        if operation:
            if operation['status'] >= 1:
                # if executed don't update
                log.warning("Event :: MocQueue_UnhandledError :: bucket: {0} :: Skipping writting to database is already in status 1".format(
                    self.bucket_index))
                return d_oper, parsed

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        return d_oper, parsed


class EventMocQueueOperationQueued(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):
        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_OperationQueued')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        # Operation Type:
        #
        # 0 none
        # 1 mintTC
        # 2 redeemTC
        # 3 mintTP
        # 4 redeemTP
        # 5 mintTCandTP
        # 6 redeemTCandTP
        # 7 swapTCforTP
        # 8 swapTPforTC
        # 9 swapTPforTP

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["bucket_"] = sanitize_address(parsed["bucket_"])
        d_event["bucket_index"] = self.bucket_index
        d_event["operType_"] = int(parsed["operType_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocQueue_OperationQueued :: bucket: {0} :: operId_: {1}".format(
            self.bucket_index, d_event["operId_"]))
        log.info(d_event)

        # write to collection operations as queue operation
        collection = self.connection_helper.mongo_collection('operations')

        # getting the information from the MoCQueue, but take in consideration that
        # after the execution of the queue this is information is no longer available
        operation = None
        d_params = dict()
        if d_event["operType_"] == 1:
            operation = 'TCMint'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsMintTC(d_event["operId_"]).call()
            d_params['qTC'] = str(raw_params[0])
            d_params['qACmax'] = str(raw_params[1])
            d_params['sender'] = sanitize_address(raw_params[2])
            d_params['recipient'] = sanitize_address(raw_params[3])
            d_params['vendor'] = sanitize_address(raw_params[4])
        elif d_event["operType_"] == 2:
            operation = 'TCRedeem'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsRedeemTC(d_event["operId_"]).call()
            d_params['qTC'] = str(raw_params[0])
            d_params['qACmin'] = str(raw_params[1])
            d_params['sender'] = sanitize_address(raw_params[2])
            d_params['recipient'] = sanitize_address(raw_params[3])
            d_params['vendor'] = sanitize_address(raw_params[4])
        elif d_event["operType_"] == 3:
            operation = 'TPMint'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsMintTP(d_event["operId_"]).call()
            d_params['tp'] = sanitize_address(raw_params[0])
            if d_params['tp']:
                d_params['tpIndex'] = self.contracts_addresses["TP"].index(d_params['tp'].lower())
            else:
                # by default the first one
                d_params['tpIndex'] = 0
            d_params['qTP'] = str(raw_params[1])
            d_params['qACmax'] = str(raw_params[2])
            d_params['sender'] = sanitize_address(raw_params[3])
            d_params['recipient'] = sanitize_address(raw_params[4])
            d_params['vendor'] = sanitize_address(raw_params[5])
        elif d_event["operType_"] == 4:
            operation = 'TPRedeem'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsRedeemTP(d_event["operId_"]).call()
            d_params['tp'] = sanitize_address(raw_params[0])
            if d_params['tp']:
                d_params['tpIndex'] = self.contracts_addresses["TP"].index(d_params['tp'].lower())
            else:
                # by default the first one
                d_params['tpIndex'] = 0
            d_params['qTP'] = str(raw_params[1])
            d_params['qACmin'] = str(raw_params[2])
            d_params['sender'] = sanitize_address(raw_params[3])
            d_params['recipient'] = sanitize_address(raw_params[4])
            d_params['vendor'] = sanitize_address(raw_params[5])
        elif d_event["operType_"] == 5:
            operation = 'TCandTPMint'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsMintTCandTP(d_event["operId_"]).call()
            d_params['tp'] = sanitize_address(raw_params[0])
            if d_params['tp']:
                d_params['tpIndex'] = self.contracts_addresses["TP"].index(d_params['tp'].lower())
            else:
                # by default the first one
                d_params['tpIndex'] = 0
            d_params['qTP'] = str(raw_params[1])
            d_params['qACmax'] = str(raw_params[2])
            d_params['sender'] = sanitize_address(raw_params[3])
            d_params['recipient'] = sanitize_address(raw_params[4])
            d_params['vendor'] = sanitize_address(raw_params[5])
        elif d_event["operType_"] == 6:
            operation = 'TCandTPRedeem'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsRedeemTCandTP(d_event["operId_"]).call()
            d_params['tp'] = sanitize_address(raw_params[0])
            if d_params['tp']:
                d_params['tpIndex'] = self.contracts_addresses["TP"].index(d_params['tp'].lower())
            else:
                # by default the first one
                d_params['tpIndex'] = 0
            d_params['qTC'] = str(raw_params[1])
            d_params['qTP'] = str(raw_params[2])
            d_params['qACmin'] = str(raw_params[3])
            d_params['sender'] = sanitize_address(raw_params[4])
            d_params['recipient'] = sanitize_address(raw_params[5])
            d_params['vendor'] = sanitize_address(raw_params[6])
        elif d_event["operType_"] == 7:
            operation = 'TCSwapForTP'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsSwapTCforTP(d_event["operId_"]).call()
            d_params['tp'] = sanitize_address(raw_params[0])
            if d_params['tp']:
                d_params['tpIndex'] = self.contracts_addresses["TP"].index(d_params['tp'].lower())
            else:
                # by default the first one
                d_params['tpIndex'] = 0
            d_params['qTC'] = str(raw_params[1])
            d_params['qTPmin'] = str(raw_params[2])
            d_params['qACmax'] = str(raw_params[3])
            d_params['sender'] = sanitize_address(raw_params[4])
            d_params['recipient'] = sanitize_address(raw_params[5])
            d_params['vendor'] = sanitize_address(raw_params[6])
        elif d_event["operType_"] == 8:
            operation = 'TPSwapForTC'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsSwapTPforTC(d_event["operId_"]).call()
            d_params['tp'] = sanitize_address(raw_params[0])
            if d_params['tp']:
                d_params['tpIndex'] = self.contracts_addresses["TP"].index(d_params['tp'].lower())
            else:
                # by default the first one
                d_params['tpIndex'] = 0
            d_params['qTP'] = str(raw_params[1])
            d_params['qTCmin'] = str(raw_params[2])
            d_params['qACmax'] = str(raw_params[3])
            d_params['sender'] = sanitize_address(raw_params[4])
            d_params['recipient'] = sanitize_address(raw_params[5])
            d_params['vendor'] = sanitize_address(raw_params[6])
        elif d_event["operType_"] == 9:
            operation = 'TPSwapForTP'
            raw_params = self.contracts_loaded["MocQueue"][self.bucket_index].sc.functions.operationsSwapTPforTP(d_event["operId_"]).call()
            d_params['tpFrom'] = sanitize_address(raw_params[0])
            if d_params['tpFrom']:
                d_params['tpFromIndex'] = self.contracts_addresses["TP"].index(d_params['tpFrom'].lower())
            else:
                d_params['tpFromIndex'] = 0
            d_params['tpTo'] = sanitize_address(raw_params[1])
            if d_params['tpTo']:
                d_params['tpToIndex'] = self.contracts_addresses["TP"].index(d_params['tpTo'].lower())
            else:
                d_params['tpToIndex'] = 0
            d_params['qTP'] = str(raw_params[2])
            d_params['qTPmin'] = str(raw_params[3])
            d_params['qACmax'] = str(raw_params[4])
            d_params['sender'] = sanitize_address(raw_params[5])
            d_params['recipient'] = sanitize_address(raw_params[6])
            d_params['vendor'] = sanitize_address(raw_params[7])

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = oper_id_to_int(d_event["operId_"])
        d_oper["bucket_index"] = self.bucket_index
        d_params['hash'] = tx_hash
        d_params['blockNumber'] = int(parsed["blockNumber"])
        d_params["createdAt"] = parsed["createdAt"]
        d_params["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["params"] = d_params
        d_oper["operation"] = operation
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = d_oper['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_QUEUED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        operation = collection.find_one({"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]})
        if operation:
            if operation['status'] >= 1:
                # if executed don't update
                log.warning("Event :: MocQueue_OperationQueued :: bucket: {0} :: Skipping writing to database is already in status 1".format(
                    self.bucket_index))
                return d_oper, parsed

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        return d_oper, parsed


class EventMocQueueOperationExecuted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection OperationQueueStatus
        collection = self.connection_helper.mongo_collection('event_MocQueue_OperationExecuted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"]) #int(parsed["operId_"].split('0x')[1])
        d_event["executor"] = sanitize_address(parsed["executor"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: MocQueue_OperationExecuted :: bucket: {0} :: operId_: {1}".format(
            self.bucket_index, d_event["operId_"]))
        log.info(d_event)

        return d_event, parsed


class EventMocQueueTCMinted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TCMinted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTC_"] = str(parsed["qTC_"])
        d_event["qAC_"] = str(parsed["qAC_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        # write to collection operations
        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TCMint'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed["gasUsed"] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTCRedeemed(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TCRedeemed')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTC_"] = str(parsed["qTC_"])
        d_event["qAC_"] = str(parsed["qAC_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        # write to collection operations
        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TCRedeem'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTPMinted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TPMinted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index

        if 'tp' in parsed:
            tp_key_name = 'tp'
        else:
            tp_key_name = 'tp_'

        d_event["tp"] = sanitize_address(parsed[tp_key_name])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTP_"] = str(parsed["qTP_"])
        d_event["qAC_"] = str(parsed["qAC_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)
                        
        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TPMint'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTPRedeemed(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TPRedeemed')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["tp_"] = sanitize_address(parsed["tp_"])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTP_"] = str(parsed["qTP_"])
        d_event["qAC_"] = str(parsed["qAC_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["bucket_index"] = self.bucket_index
        d_oper["operId_"] = d_event["operId_"]
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TPRedeem'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTPSwappedForTP(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TPSwappedForTP')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["tpFrom_"] = sanitize_address(parsed["tpFrom_"])
        d_event['tpFromIndex_'] = self.contracts_addresses['TP'].index(d_event["tpFrom_"].lower())
        d_event["tpTo_"] = sanitize_address(parsed["tpTo_"])
        d_event['tpToIndex_'] = self.contracts_addresses['TP'].index(d_event["tpTo_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTPfrom_"] = str(parsed["qTPfrom_"])
        d_event["qTPto_"] = str(parsed["qTPto_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TPSwapForTP'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTPSwappedForTC(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TPSwappedForTC')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["tp_"] = sanitize_address(parsed["tp_"])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTC_"] = str(parsed["qTC_"])
        d_event["qTP_"] = str(parsed["qTP_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["bucket_index"] = self.bucket_index
        d_oper["operId_"] = d_event["operId_"]
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TPSwapForTC'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTCSwappedForTP(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TCSwappedForTP')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["tp_"] = sanitize_address(parsed["tp_"])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTC_"] = str(parsed["qTC_"])
        d_event["qTP_"] = str(parsed["qTP_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TCSwapForTP'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTCandTPRedeemed(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):
        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TCandTPRedeemed')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["tp_"] = sanitize_address(parsed["tp_"])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTC_"] = str(parsed["qTC_"])
        d_event["qTP_"] = str(parsed["qTP_"])
        d_event["qAC_"] = str(parsed["qAC_"])
        d_event["qACtoRedeemTC_"] = str(parsed["qACtoRedeemTC_"])
        d_event["qACtoRedeemTP_"] = str(parsed["qACtoRedeemTP_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TCandTPRedeem'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventMocQueueTCandTPMinted(BaseEvent):

    def __init__(self,
                 options,
                 connection_helper,
                 contracts_loaded,
                 contracts_addresses,
                 filter_contracts_addresses,
                 block_info,
                 bucket_index):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.bucket_index = bucket_index

        super().__init__(options,
                         connection_helper,
                         contracts_loaded,
                         contracts_addresses,
                         filter_contracts_addresses,
                         block_info)

    def parse_event_and_save(self, parsed_receipt, decoded_event):
        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_MocQueue_TCandTPMinted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = OrderedDict()
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["bucket_index"] = self.bucket_index
        d_event["tp_"] = sanitize_address(parsed["tp_"])
        d_event['tpIndex_'] = self.contracts_addresses['TP'].index(d_event["tp_"].lower())
        d_event["sender_"] = sanitize_address(parsed["sender_"])
        d_event["recipient_"] = sanitize_address(parsed["recipient_"])
        d_event["qTC_"] = str(parsed["qTC_"])
        d_event["qTP_"] = str(parsed["qTP_"])
        d_event["qAC_"] = str(parsed["qAC_"])
        d_event["qACtoMintTC_"] = str(parsed["qACtoMintTC_"])
        d_event["qACtoMintTP_"] = str(parsed["qACtoMintTP_"])
        d_event["qACfee_"] = str(parsed["qACfee_"])
        d_event["qFeeToken_"] = str(parsed["qFeeToken_"])
        d_event["qACVendorMarkup_"] = str(parsed["qACVendorMarkup_"])
        d_event["qFeeTokenVendorMarkup_"] = str(parsed["qFeeTokenVendorMarkup_"])
        d_event["vendor_"] = sanitize_address(parsed["vendor_"])
        d_event["operId_"] = oper_id_to_int(parsed["operId_"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        collection = self.connection_helper.mongo_collection('operations')

        # STATUS:
        # -4 Revert
        # -3 Stale Transaction
        # -2 Error Unhandled
        # -1 Error
        #  0 Queue
        #  1 Executed
        #  2 Confirmed > 10 blocks

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["operId_"] = d_event["operId_"]
        d_oper["bucket_index"] = self.bucket_index
        d_oper["executed"] = d_event
        d_oper["operation"] = 'TCandTPMint'
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed["gasPrice"]), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"operId_": d_oper["operId_"], "bucket_index": d_oper["bucket_index"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Event MocQueue {0} :: bucket: {1} :: operId_: {2}".format(
            d_oper["operation"], self.bucket_index, d_oper["operId_"]))

        return d_oper


class EventTokenTransfer(BaseEvent):

    def __init__(self, options, connection_helper, contracts_loaded, contracts_addresses, filter_contracts_addresses, block_info, token_involved):

        self.options = options
        self.connection_helper = connection_helper
        self.contracts_loaded = contracts_loaded
        self.filter_contracts_addresses = filter_contracts_addresses
        self.block_info = block_info
        self.token_involved = token_involved

        super().__init__(options, connection_helper, contracts_loaded, contracts_addresses, filter_contracts_addresses, block_info)

    # def parse_event(self, parsed_receipt, decoded_event):
    #
    #     # decode event to support write in mongo
    #     parsed_receipt['from'] = decoded_event['from'].lower()
    #     parsed_receipt['to'] = decoded_event['to'].lower()
    #     parsed_receipt['value'] = str(decoded_event['value'])
    #
    #     return parsed_receipt

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        address_from_contract = '0x0000000000000000000000000000000000000000'
        address_not_allowed = [str.lower(address_from_contract)] + self.filter_contracts_addresses

        if sanitize_address(parsed['from']).lower() in address_not_allowed or \
                sanitize_address(parsed['to']).lower() in address_not_allowed:
            # skip transfers to our contracts
            return parsed

        # get collection
        collection = self.connection_helper.mongo_collection('operations')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_oper = OrderedDict()
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'Transfer'
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["gas"] = parsed['gas']
        d_oper["gasPrice"] = str(parsed['gasPrice'])
        d_oper["gasUsed"] = int(parsed['gasUsed'])
        gas_fee = parsed['gasUsed'] * Web3.from_wei(int(parsed['gasPrice']), 'ether')
        d_oper["gasFeeRBTC"] = str(int(gas_fee * self.precision))
        d_oper["status"] = TX_STATUS_EXECUTED
        d_params = dict()
        d_params['hash'] = tx_hash
        d_params['blockNumber'] = int(parsed["blockNumber"])
        d_params["createdAt"] = parsed["createdAt"]
        d_params["lastUpdatedAt"] = datetime.datetime.now()
        d_params["token"] = self.token_involved
        d_params["sender"] = sanitize_address(parsed["from"])
        d_params["recipient"] = sanitize_address(parsed["to"])
        d_params["amount"] = str(parsed["value"])
        d_oper["params"] = d_params
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["confirmationTime"] = None
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_oper["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        log.info("Tx {0} - Token: [{1}] From: [{2}] To: [{3}] Value: [{4}] Tx Hash: [{5}]".format(
            'Transfer',
            d_params["token"],
            d_params["sender"],
            d_params["recipient"],
            d_params["amount"],
            tx_hash))

        return d_oper, parsed


class EventOMOCIncentiveV2ClaimOK(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_IncentiveV2_ClaimOK')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["origin"] = sanitize_address(parsed["origin"]).lower()
        d_event["value"] = str(parsed["value"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: IncentiveV2_ClaimOK :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventOMOCVestingFactoryVestingCreated(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_VestingFactory_VestingCreated')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["vesting"] = sanitize_address(parsed["vesting"]).lower()
        d_event["holder"] = sanitize_address(parsed["holder"]).lower()
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: VestingFactory_VestingCreated :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventOMOCDelayMachinePaymentCancel(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_DelayMachine_PaymentCancel')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["id"] = oper_id_to_int(parsed["id"])
        d_event["source"] = sanitize_address(parsed["source"]).lower()
        d_event["destination"] = sanitize_address(parsed["destination"]).lower()
        d_event["amount"] = str(parsed["amount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: DelayMachine_PaymentCancel :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        # Write to Omoc Operation collection
        collection = self.connection_helper.mongo_collection('omoc_operations')
        d_oper = OrderedDict()
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'DelayMachine_PaymentCancel'
        d_oper["id"] = oper_id_to_int(parsed["id"])
        d_oper["source"] = sanitize_address(parsed["source"]).lower()
        d_oper["destination"] = sanitize_address(parsed["destination"]).lower()
        d_oper["amount"] = str(parsed["amount"])
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        return d_event, parsed


class EventOMOCDelayMachinePaymentDeposit(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_DelayMachine_PaymentDeposit')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["id"] = oper_id_to_int(parsed["id"])
        d_event["source"] = sanitize_address(parsed["source"]).lower()
        d_event["destination"] = sanitize_address(parsed["destination"]).lower()
        d_event["amount"] = str(parsed["amount"])
        d_event["expiration"] = int(parsed["expiration"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: DelayMachine_PaymentDeposit :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        # Write to Omoc Operation collection
        collection = self.connection_helper.mongo_collection('omoc_operations')
        d_oper = OrderedDict()
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'DelayMachine_PaymentDeposit'
        d_oper["id"] = oper_id_to_int(parsed["id"])
        d_oper["source"] = sanitize_address(parsed["source"]).lower()
        d_oper["destination"] = sanitize_address(parsed["destination"]).lower()
        d_oper["amount"] = str(parsed["amount"])
        d_oper["expiration"] = int(parsed["expiration"])
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        return d_event, parsed


class EventOMOCDelayMachinePaymentWithdraw(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_DelayMachine_PaymentWithdraw')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["id"] = oper_id_to_int(parsed["id"])
        d_event["source"] = sanitize_address(parsed["source"]).lower()
        d_event["destination"] = sanitize_address(parsed["destination"]).lower()
        d_event["amount"] = str(parsed["amount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: DelayMachine_PaymentWithdraw :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        # Write to Omoc Operation collection
        collection = self.connection_helper.mongo_collection('omoc_operations')
        d_oper = OrderedDict()
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'DelayMachine_PaymentWithdraw'
        d_oper["id"] = oper_id_to_int(parsed["id"])
        d_oper["source"] = sanitize_address(parsed["source"]).lower()
        d_oper["destination"] = sanitize_address(parsed["destination"]).lower()
        d_oper["amount"] = str(parsed["amount"])
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        return d_event, parsed


class EventOMOCSupportersAddStake(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Supporters_AddStake')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_event["sender"] = sanitize_address(parsed["sender"]).lower()
        d_event["amount"] = str(parsed["amount"])
        d_event["mocs"] = str(parsed["mocs"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Supporters_AddStake {0}".format(d_event["id_event"]))

        # Write to Omoc Operation collection
        collection = self.connection_helper.mongo_collection('omoc_operations')
        d_oper = OrderedDict()
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'Supporters_AddStake'
        d_oper["user"] = sanitize_address(parsed["user"]).lower()
        d_oper["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_oper["sender"] = sanitize_address(parsed["sender"]).lower()
        d_oper["amount"] = str(parsed["amount"])
        d_oper["mocs"] = str(parsed["mocs"])
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        return d_event, parsed


class EventOMOCSupportersCancelEarnings(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Supporters_CancelEarnings')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["earnings"] = str(parsed["earnings"])
        d_event["start"] = int(parsed["start"])
        d_event["end"] = int(parsed["end"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Supporters_CancelEarnings :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventOMOCSupportersPayEarnings(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Supporters_PayEarnings')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["earnings"] = str(parsed["earnings"])
        d_event["start"] = int(parsed["start"])
        d_event["end"] = int(parsed["end"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Supporters_PayEarnings :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventOMOCSupportersWithdraw(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Supporters_Withdraw')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["msgSender"] = sanitize_address(parsed["msgSender"]).lower()
        d_event["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_event["receiver"] = sanitize_address(parsed["receiver"]).lower()
        d_event["mocs"] = str(parsed["mocs"])
        d_event["blockNum"] = int(parsed["blockNumber"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Supporters_Withdraw :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        # Write to Omoc Operation collection
        collection = self.connection_helper.mongo_collection('omoc_operations')
        d_oper = OrderedDict()
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'Supporters_Withdraw'
        d_oper["msgSender"] = sanitize_address(parsed["msgSender"]).lower()
        d_oper["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_oper["receiver"] = sanitize_address(parsed["receiver"]).lower()
        d_oper["amount"] = str(parsed["mocs"])
        d_oper["mocs"] = str(parsed["mocs"])
        d_oper["blockNum"] = int(parsed["blockNumber"])
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        return d_event, parsed


class EventOMOCSupportersWithdrawStake(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_Supporters_WithdrawStake')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_event["destination"] = sanitize_address(parsed["destination"]).lower()
        d_event["amount"] = str(parsed["amount"])
        d_event["mocs"] = str(parsed["mocs"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id and replace with id_event as unique id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Supporters_WithdrawStake :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        # Write to Omoc Operation collection
        collection = self.connection_helper.mongo_collection('omoc_operations')
        d_oper = OrderedDict()
        d_oper["hash"] = tx_hash
        d_oper["id_event"] = id_event
        d_oper["blockNumber"] = int(parsed["blockNumber"])
        d_oper["operation"] = 'Supporters_WithdrawStake'
        d_oper["user"] = sanitize_address(parsed["user"]).lower()
        d_oper["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_oper["destination"] = sanitize_address(parsed["destination"]).lower()
        d_oper["amount"] = str(parsed["amount"])
        d_oper["mocs"] = str(parsed["mocs"])
        d_oper["createdAt"] = parsed["createdAt"]
        d_oper["lastUpdatedAt"] = datetime.datetime.now()
        d_oper["last_block_indexed"] = int(parsed["blockNumber"])

        collection.find_one_and_update(
            {"id_event": d_oper["id_event"]},
            {"$set": d_oper},
            upsert=True)

        return d_event, parsed


class EventOMOCVotingMachineVoteEvent(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        # get collection
        collection = self.connection_helper.mongo_collection('event_VotingMachine_VoteEvent')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["subaccount"] = sanitize_address(parsed["subaccount"]).lower()
        d_event["destination"] = sanitize_address(parsed["destination"]).lower()
        d_event["amount"] = str(parsed["amount"])
        d_event["mocs"] = str(parsed["mocs"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        # remove old document with only hash as id
        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: VotingMachine_VoteEvent :: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


# ---------------------------------------------------------------------------
# Lending and Borrowing events (MocLendingManager / MocLendingQueue)
# ---------------------------------------------------------------------------

LENDING_OPER_TYPE = {0: 'NONE', 1: 'BORROW', 2: 'REMOVE_AC_FROM_VAULT', 3: 'REPAY_WITH_AC'}


class EventLendingDeposit(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_Deposit')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["tpAmount"] = str(parsed["tpAmount"])
        d_event["depositUnits"] = str(parsed["depositUnits"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_Deposit :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingWithdraw(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_Withdraw')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["depositUnits"] = str(parsed["depositUnits"])
        d_event["tpAmount"] = str(parsed["tpAmount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_Withdraw :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingAddACtoVault(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_AddACtoVault')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["acAmount"] = str(parsed["acAmount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_AddACtoVault :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingRemoveACfromVault(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_RemoveACfromVault')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["acAmount"] = str(parsed["acAmount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_RemoveACfromVault :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingBorrow(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_Borrow')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["tpAmount"] = str(parsed["tpAmount"])
        d_event["creditUnits"] = str(parsed["creditUnits"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_Borrow :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingRepay(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_Repay')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["creditUnits"] = str(parsed["creditUnits"])
        d_event["tpAmount"] = str(parsed["tpAmount"])
        d_event["tpToFeeFlow"] = str(parsed["tpToFeeFlow"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_Repay :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingRepayWithAC(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_RepayWithAC')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["creditUnits"] = str(parsed["creditUnits"])
        d_event["acSold"] = str(parsed["acSold"])
        d_event["tpAmount"] = str(parsed["tpAmount"])
        d_event["tpToFeeFlow"] = str(parsed["tpToFeeFlow"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_RepayWithAC :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingLiquidate(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_Liquidate')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["liquidator"] = sanitize_address(parsed["liquidator"]).lower()
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["acSwapped"] = str(parsed["acSwapped"])
        d_event["tpPaid"] = str(parsed["tpPaid"])
        d_event["tpToFeeFlow"] = str(parsed["tpToFeeFlow"])
        d_event["isComplete"] = bool(parsed["isComplete"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_Liquidate :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingTPInjection(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_TPInjection')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["tpAmount"] = str(parsed["tpAmount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_TPInjection :: id: {0}".format(d_event["id_event"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingOperationQueued(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_OperationQueued')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        oper_type_int = int(parsed["operType"])

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["operId"] = int(parsed["operId"])
        d_event["operType"] = oper_type_int
        d_event["operTypeName"] = LENDING_OPER_TYPE.get(oper_type_int, 'UNKNOWN')
        d_event["user"] = sanitize_address(parsed["user"]).lower()
        d_event["recipient"] = sanitize_address(parsed["recipient"]).lower()
        d_event["tpToken"] = sanitize_address(parsed["tpToken"])
        d_event["mocBucket"] = sanitize_address(parsed["mocBucket"])
        d_event["amount"] = str(parsed["amount"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_OperationQueued :: operId: {0} type: {1}".format(
            d_event["operId"], d_event["operTypeName"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingOperationError(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_OperationError')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["operId"] = int(parsed["operId"])
        d_event["reason"] = parsed["reason"].hex() if isinstance(parsed["reason"], (bytes, bytearray)) else str(parsed["reason"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_OperationError :: operId: {0}".format(d_event["operId"]))
        log.info(d_event)

        return d_event, parsed


class EventLendingOperationExecuted(BaseEvent):

    def parse_event_and_save(self, parsed_receipt, decoded_event):

        parsed = self.parse_event(parsed_receipt, decoded_event)

        collection = self.connection_helper.mongo_collection('event_Lending_OperationExecuted')

        tx_hash = parsed['hash']
        log_index = parsed['logIndex']
        id_event = "{0}:{1}".format(tx_hash, log_index)

        d_event = dict()
        d_event["hash"] = tx_hash
        d_event["id_event"] = id_event
        d_event["blockNumber"] = int(parsed["blockNumber"])
        d_event["executor"] = sanitize_address(parsed["executor"]).lower()
        d_event["operId"] = int(parsed["operId"])
        d_event["createdAt"] = parsed["createdAt"]
        d_event["lastUpdatedAt"] = datetime.datetime.now()

        remove_query = {"hash": d_event["hash"], "id_event": {"$exists": False}}
        if collection.find(remove_query):
            collection.delete_many(remove_query)

        collection.find_one_and_update(
            {"id_event": d_event["id_event"]},
            {"$set": d_event},
            upsert=True)

        log.info("Event :: Lending_OperationExecuted :: operId: {0}".format(d_event["operId"]))
        log.info(d_event)

        return d_event, parsed
