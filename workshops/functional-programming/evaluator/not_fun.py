import csv


class Applicant(object):

    def __init__(self, applicant_id, is_credible, credit_score, experience_years, criminal_record):
        self._applicant_id = int(applicant_id)
        self._is_credible = bool(int(is_credible))
        self._credit_score = int(credit_score)
        self._experience_years = int(experience_years)
        self._criminal_record = bool(int(criminal_record))

    def get_applicant_id(self):
        return self._applicant_id

    def is_credible(self):
        return self._is_credible

    def get_credit_score(self):
        return self._credit_score

    def get_experience_years(self):
        return self._experience_years

    def has_criminal_record(self):
        return self._criminal_record

    def __str__(self):
        return '{is_credible=%s, credit_score=%s, experience_years=%s, criminal_record=%s}' % (self._is_credible, self._credit_score, self._experience_years, self._criminal_record)


class Evaluator(object):

    def evaluate(self, applicant):
        raise Exception("Not implemented")


class QualifiedEvaluator(Evaluator):

    def evaluate(self, applicant):
        return applicant.is_credible()


class EvaluatorChain(Evaluator):

    def __init__(self, next_evaluator):
        self.next_evaluator = next_evaluator

    def evaluate(self, applicant):
        return self.next_evaluator.evaluate(applicant)


class CreditEvaluator(EvaluatorChain):

    def evaluate(self, applicant):
        if applicant.get_credit_score() > 600:
            return super(CreditEvaluator, self).evaluate(applicant)
        else:
            return False


class ExperienceEvaluator(EvaluatorChain):

    def evaluate(self, applicant):
        if applicant.get_experience_years() > 2:
            return super(ExperienceEvaluator, self).evaluate(applicant)
        else:
            return False


class CriminalRecordsEvaluator(EvaluatorChain):

    def evaluate(self, applicant):
        if not applicant.has_criminal_record():
            return super(CriminalRecordsEvaluator, self).evaluate(applicant)
        else:
            return False


if __name__ == "__main__":

    evaluator1 = CreditEvaluator(QualifiedEvaluator())
    evaluator2 = CreditEvaluator(ExperienceEvaluator(QualifiedEvaluator()))
    evaluator3 = CriminalRecordsEvaluator(ExperienceEvaluator(QualifiedEvaluator()))
    evaluator4 = CriminalRecordsEvaluator(CreditEvaluator(ExperienceEvaluator(QualifiedEvaluator())))

    with open('evaluator/applicants.csv') as applicants_data:
        result = dict()

        total1 = 0
        total2 = 0
        total3 = 0
        total4 = 0

        for data in csv.DictReader(applicants_data):
            applicant = Applicant(**data)

            if evaluator1.evaluate(applicant):
                total1 += 1

            if evaluator2.evaluate(applicant):
                total2 += 1

            if evaluator3.evaluate(applicant):
                total3 += 1

            if evaluator4.evaluate(applicant):
                total4 += 1

        print('1: %s, 2: %s, 3: %s, 4: %s' % (total1, total2, total3, total4))
