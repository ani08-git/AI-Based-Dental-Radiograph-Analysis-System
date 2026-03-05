def generate_report(data):

    detected = data["detected_teeth"]

    expected_teeth = 32

    missing = expected_teeth - detected

    report = {
        "expected_teeth": expected_teeth,
        "detected_teeth": detected,
        "missing_teeth": missing
    }

    return report