import os
from enum import Enum
from typing import Dict
from dotenv import load_dotenv
from pydantic import BaseModel, RootModel
import google.generativeai as genai
import instructor
from sample_logs import task_adobe__spectrum_web_components_5118

load_dotenv()


genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

class TestResult(str, Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"

class TestResults(RootModel[Dict[str, TestResult]]):
    pass

class LogParsedResults(BaseModel):
    test_results: TestResults
    all_success: bool
    all_failed: bool

def main():
    client = instructor.from_gemini(
        client=model,
        mode=instructor.Mode.GEMINI_JSON,
    )

    prompt = f"""
    Analyze this test log and extract test results as JSON.
Schema: {LogParsedResults.model_json_schema()}
We are looking for actual test names not test files.
If you think all tests passed, set all_success to true, even if you cannot find individual test results.
If you think all tests failed, set all_failed to true, even if you cannot find individual test results.

Log: {task_adobe__spectrum_web_components_5118}

It is essential for the test names to be actual test names, not test files, not test suites, not a test runner, etc.
If there is an error preventing the test from running, and we cannot find any test results, all_failed should be true.
    """

    response: LogParsedResults = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
        ],
        response_model=LogParsedResults,
    )
    response_dict = response.model_dump()
    success_count = sum(1 for result in response_dict['test_results'].values() if result == TestResult.PASSED)
    failed_count = sum(1 for result in response_dict['test_results'].values() if result == TestResult.FAILED)
    print(f"Success count: {success_count}")
    print(f"Failed count: {failed_count}")
    print(f"All success: {response_dict['all_success']}")
    print(f"All failed: {response_dict['all_failed']}")

if __name__ == "__main__":
    main()
