import json

from datetime import datetime
from pathlib import Path


# =========================================================
# SYNERGIA BUSINESS VALIDATOR
# STAGE 6.3.11
# =========================================================


print("[BUSINESS VALIDATOR LOADED]")


# =========================================================
# REQUIRED FILES
# =========================================================


REQUIRED_FILES = {

    "website": (
        "website",
        "website.txt"
    ),

    "branding": (
        "branding",
        "branding.txt"
    ),

    "social": (
        "social",
        "social.txt"
    ),

    "docs": (
        "docs",
        "docs.txt"
    )

}


# =========================================================
# VALIDATE PROJECT
# =========================================================


def validate_project(

    project_path

):

    project = Path(
        project_path
    )


    print(
        "\n[BUSINESS VALIDATION]"
    )

    print(
        project
    )


    # =====================================================
    # PROJECT EXISTS
    # =====================================================


    if not project.exists():

        result = {

            "status": "INVALID",

            "project": str(
                project
            ),

            "score": 0,

            "checks": {},

            "errors": [

                "Project directory does not exist"
            ],

            "validated_at": (
                datetime.now()
                .isoformat()
            )

        }


        print(
            "\n[VALIDATION FAILED]"
        )

        print(
            "Project directory does not exist"
        )


        return result


    # =====================================================
    # CHECK FILES
    # =====================================================


    checks = {}

    errors = []

    approved = 0

    total = len(
        REQUIRED_FILES
    )


    for module, file_data in (
        REQUIRED_FILES.items()
    ):


        directory = file_data[0]

        filename = file_data[1]


        file_path = (

            project

            / directory

            / filename

        )


        check = {

            "file": str(
                file_path
            ),

            "exists": False,

            "has_content": False,

            "size_bytes": 0,

            "status": "FAILED"

        }


        # =================================================
        # FILE EXISTS
        # =================================================


        if file_path.exists():

            check["exists"] = True


            size = file_path.stat().st_size


            check["size_bytes"] = size


            # =============================================
            # FILE HAS CONTENT
            # =============================================


            if size > 0:

                check[
                    "has_content"
                ] = True


                check[
                    "status"
                ] = "OK"


                approved += 1


            else:

                errors.append(

                    f"{module}: "
                    "file is empty"

                )


        else:

            errors.append(

                f"{module}: "
                "required file not found"

            )


        checks[module] = check


        print(

            f"[CHECK] "

            f"{module.upper()} "

            f"=> "

            f"{check['status']}"

        )


    # =====================================================
    # SCORE
    # =====================================================


    score = round(

        (

            approved

            / total

        )

        * 100,

        2

    )


    # =====================================================
    # FINAL STATUS
    # =====================================================


    if approved == total:

        status = "VALID"


    elif approved > 0:

        status = "PARTIAL"


    else:

        status = "INVALID"


    # =====================================================
    # RESULT
    # =====================================================


    result = {

        "status": status,

        "project": str(
            project
        ),

        "score": score,

        "approved": approved,

        "total_checks": total,

        "checks": checks,

        "errors": errors,

        "validated_at": (
            datetime.now()
            .isoformat()
        )

    }


    # =====================================================
    # SAVE REPORT
    # =====================================================


    report_file = (

        project

        / "validation_report.json"

    )


    with open(

        report_file,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            result,

            file,

            indent=2,

            ensure_ascii=False

        )


    result[
        "report"
    ] = str(
        report_file
    )


    # =====================================================
    # FINAL OUTPUT
    # =====================================================


    print(

        "\n[VALIDATION FINISHED]"

    )


    print(

        f"STATUS: {status}"

    )


    print(

        f"SCORE: {score}%"

    )


    print(

        f"APPROVED: "

        f"{approved}/{total}"

    )


    print(

        f"REPORT: "

        f"{report_file}"

    )


    return result
