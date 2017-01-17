import csv
import functools


def p_compose(*predicates):
    # TODO Implement. This function should take a set of predicates and combine
    # them into one. The resulting predicate is true if and only if all predicates
    # are also true
    raise Exception("Not implemented")


if __name__ == "__main__":
    qualifed_evaluator = lambda applicant: bool(int(applicant['is_credible']))
    credit_evaluator = lambda applicant: int(applicant['credit_score']) > 600
    experience_evaluator = lambda applicant: int(applicant['experience_years']) > 2
    criminal_record_evaluator = lambda applicant: not bool(int(applicant['criminal_record']))

    evaluator1 = p_compose(credit_evaluator, qualifed_evaluator)
    evaluator2 = p_compose(credit_evaluator, experience_evaluator, qualifed_evaluator)
    evaluator3 = p_compose(criminal_record_evaluator, experience_evaluator, qualifed_evaluator)
    evaluator4 = p_compose(criminal_record_evaluator, credit_evaluator, experience_evaluator, qualifed_evaluator)

    with open('evaluator/applicants.csv') as applicants_data:
        results = map(
            lambda applicant: (evaluator1(applicant), evaluator2(applicant),
                               evaluator3(applicant), evaluator4(applicant)),
            csv.DictReader(applicants_data)
        )

        def totals_reducer(accumlator, evaluator_result):
            return map(
                lambda t: t[0] + 1 if t[1] else t[0],  # t[0]: total and t[1]: result
                zip(accumlator, evaluator_result)
            )

        totals = functools.reduce(
            totals_reducer,
            results,
            (0, 0, 0, 0)
        )

        print('1: %s, 2: %s, 3: %s, 4: %s' % tuple(totals))
