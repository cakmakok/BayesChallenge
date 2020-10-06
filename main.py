from code_challenge import CodeChallengeImplementation
import solutions


def load(message_id: int) -> str:
    """ Do not change this function. """
    with open(f"data/data_{message_id:03d}", "r") as file:
        return file.read()


def run(*nums: int) -> CodeChallengeImplementation:
    """ Do not change this function. """
    merger = CodeChallengeImplementation()

    for message_id in nums:
        message = load(message_id)

        merger.merge(message)

    return merger


if __name__ == '__main__':
    """
    This is a set of test runs and their solutions. With a fully function code challenge implementation, this should
    be executed without raising any AssertionErrors.
    """
    message_sequence_1 = [1, 2, 3, 4]

    assert run(*message_sequence_1).state() == solutions.expected_run_1_2_3_4
    assert run(*message_sequence_1).reversed_state() == solutions.expected_run_1_2_3_4_reversed

    message_sequence_10 = list(range(1, 100))
    assert run(*message_sequence_10).state() == solutions.expected_run_1_to_99
