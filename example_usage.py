from client import FlakyTestTimingNonDeterminismDetectorClient

def main():
    client = FlakyTestTimingNonDeterminismDetectorClient()
    res = client.analyze_flaky_test_telemetry()
    print('Flaky Test Detector: ' + res['flakiness_audit_id'] + ' (' + res['test_suite'] + ')')
    print('Failure Rate: ' + str(res['observed_failure_rate']) + ' | Cause: ' + res['root_cause_classification'])
    print('Remediation: ' + res['recommended_remediation'])

if __name__ == '__main__':
    main()
