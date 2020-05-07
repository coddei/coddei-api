import time

worker_id_bits = 5
data_center_id_bits = 5
max_worker_id = -1 ^ (-1 << worker_id_bits)
max_data_center_id = -1 ^ (-1 << data_center_id_bits)
sequence_bits = 12
worker_id_shift = sequence_bits
data_center_id_shift = sequence_bits + worker_id_bits
timestamp_left_shift = sequence_bits + worker_id_bits + data_center_id_bits
sequence_mask = -1 ^ (-1 << sequence_bits)


class Snowflake:
    def __init__(self):
        # Thursday, 7 May 2020 01:00:00 GMT
        self.cepoch = 1588813200

    def generator(self, worker_id, data_center_id, sleep=lambda x: time.sleep(x/1000.0)):
        assert worker_id >= 0 and worker_id <= max_worker_id
        assert data_center_id >= 0 and data_center_id <= max_data_center_id

        last_timestamp = -1
        sequence = 0

        while True:
            timestamp = int(time.time()*1000)

            if last_timestamp > timestamp:
                sleep(last_timestamp-timestamp)
                continue

            if last_timestamp == timestamp:
                sequence = (sequence + 1) & sequence_mask
                if sequence == 0:
                    sequence = -1 & sequence_mask
                    sleep(1)
                    continue
            else:
                sequence = 0

            last_timestamp = timestamp

            yield (
                (timestamp-self.cepoch << timestamp_left_shift) |
                (data_center_id << data_center_id_shift) |
                (worker_id << worker_id_shift) |
                sequence)
