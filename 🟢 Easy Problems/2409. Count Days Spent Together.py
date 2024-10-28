class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_arrive_month, alice_arrive_day = map(int, arriveAlice.split("-"))
        alice_leave_month, alice_leave_day = map(int, leaveAlice.split("-"))

        bob_arrive_month, bob_arrive_day = map(int, arriveBob.split("-"))
        bob_leave_month, bob_leave_day = map(int, leaveBob.split("-"))

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        alice_arrive = sum(months[:alice_arrive_month - 1]) + alice_arrive_day
        alice_leave = sum(months[:alice_leave_month - 1]) + alice_leave_day
        bob_arrive = sum(months[:bob_arrive_month - 1]) + bob_arrive_day
        bob_leave = sum(months[:bob_leave_month - 1]) + bob_leave_day

        start = max(alice_arrive, bob_arrive)
        end = min(alice_leave, bob_leave)

        total_days = max(0, end - start + 1)

        return total_days