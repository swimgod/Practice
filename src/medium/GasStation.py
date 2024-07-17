from typing import List, Optional
import math


class GasStation:
    @staticmethod
    def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_cost > total_gas:
            return -1

        starting_index = 0
        current_gas = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        return starting_index


    @staticmethod
    def canCompleteCircuitTimeExceeded(gas: List[int], cost: List[int]) -> int:
        print(gas)
        print(cost)

        starting_indexes = {n: 0 for n in range(len(gas)) if gas[n] >= cost[n]}
        print(f"Potential Starting Indexes: {starting_indexes}")

        for i in starting_indexes:
            j = 0
            is_starting_index_last_index = i == (len(gas) - 1)
            if is_starting_index_last_index:
                j = 0
            else:
                j = i + 1
            cur_tank = gas[i] + gas[j] - cost[i]
            print(f"Current Gas: {gas[i]} + {gas[j]} - {cost[i]} = {gas[i] + gas[j] - cost[i]}")
            print(f"Starting Index: {i}")

            while j != i:
                is_current_index_last_index = j == (len(gas) - 1)
                if is_current_index_last_index:
                    print(f"Current Index: {j} and Next Index: 0 and Current Gas: {cur_tank} + {gas[0]} - {cost[j]} = {cur_tank + gas[0] - cost[j]}")
                    cur_tank -= cost[j]
                    if cur_tank >= 0:
                        j = 0
                        gas_at_next_station = gas[0]
                        cur_tank += gas_at_next_station
                    else:
                        starting_indexes[i] = -1
                        break
                else:
                    print(f"Current Index: {j} and Next Index: {j + 1} and Current Gas: {cur_tank} + {gas[j + 1]} - {cost[j]} = {cur_tank + gas[j + 1] - cost[j]}")
                    cur_tank -= cost[j]
                    if cur_tank >= 0:
                        j += 1
                        gas_at_next_station = gas[j]
                        cur_tank += gas_at_next_station
                    else:
                        starting_indexes[i] = -1
                        break
            if j == i:
                starting_indexes[i] = j

        print(starting_indexes)
        for k in starting_indexes:
            if starting_indexes[k] != -1:
                return k
        return -1