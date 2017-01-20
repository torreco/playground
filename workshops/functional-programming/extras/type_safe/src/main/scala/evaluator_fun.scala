import com.github.tototoshi.csv._

import scala.io.Source


object Evaluator {

  type Applicant = Map[String, String]
  type Evaluator = Applicant => Boolean

  def p_compose(predicates: Evaluator*): Evaluator = applicant => predicates.forall(p => p(applicant))

  def main(args: Array[String]): Unit = {

    val qualifedEvaluator = (applicant: Applicant) => applicant("is_credible").toInt == 1
    val creditEvaluator = (applicant: Applicant) => applicant("credit_score").toInt > 600
    val experienceEvaluator = (applicant: Applicant) => applicant("experience_years").toInt > 2
    val criminalRecordEvaluator = (applicant: Applicant) => applicant("criminal_record").toInt == 0

    val evaluator1 = p_compose(creditEvaluator, qualifedEvaluator)
    val evaluator2 = p_compose(creditEvaluator, experienceEvaluator, qualifedEvaluator)
    val evaluator3 = p_compose(criminalRecordEvaluator, experienceEvaluator, qualifedEvaluator)
    val evaluator4 = p_compose(criminalRecordEvaluator, creditEvaluator, experienceEvaluator, qualifedEvaluator)

    val dataSource = Source.fromURL(getClass.getResource("applicants.csv"))
    val reader = CSVReader.open(dataSource)

    val totals =
      reader.toStreamWithHeaders
        .map { applicant =>
          List(evaluator1(applicant), evaluator2(applicant), evaluator3(applicant), evaluator4(applicant))
        }
        .foldLeft(List(0, 0, 0, 0)) { (accumulator, evaluatorResult) =>
          accumulator.zip(evaluatorResult).map {
            case (total, result) => if (result) total + 1 else total
          }
        }

    println(s"1: ${totals(0)}, 2: ${totals(1)}, 3: ${totals(2)}, 4: ${totals(3)}")

  }
}
