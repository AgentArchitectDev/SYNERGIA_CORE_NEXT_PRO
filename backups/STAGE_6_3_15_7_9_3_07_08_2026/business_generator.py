from pathlib import Path
from datetime import datetime
from time import time


from ai.core.task_engine import TaskEngine


from ai.core.ai_orchestrator import (
    ai_orchestrator
)


from ai.business.project_builder import (
    create_project_structure
)


from ai.business.website_generator import (
    generate_website
)


from ai.business.branding_generator import (
    generate_branding
)


from ai.business.social_generator import (
    generate_social
)


from ai.business.docs_generator import (
    generate_docs
)


from ai.business.business_performance import (
    BusinessPerformance
)


from ai.business.adaptive_model_router import (
    AdaptiveModelRouter
)


from ai.business.business_validator import (
    validate_project
)



# =========================================================
#
# SYNERGIA BUSINESS GENERATOR
#
# STAGE 6.3.15.7.8.4
#
# BUSINESS AUTONOMOUS INTEGRATION
#
# STAGE 6.3.15.7.9.1
#
# REAL MODEL TRACKING
#
# STAGE 6.3.15.7.9.3
#
# REAL EXECUTION MODEL MEMORY FIX
#
# =========================================================


print(
    "[BUSINESS GENERATOR LOADED]"
)



# =========================================================
# CREATE BUSINESS PROJECT
# =========================================================


def create_business_project(
    prompt,
    progress_callback=None
):


    performance = BusinessPerformance()



    task_engine = TaskEngine()



    adaptive_router = AdaptiveModelRouter(
        performance.optimizer
    )



    performance.start()



    # =====================================================
    # TIMESTAMP
    # =====================================================


    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )



    # =====================================================
    # PROJECT NAME
    # =====================================================


    project_name = (

        prompt.lower()

        .replace(
            " ",
            "_"
        )

        [:30]

    )



    # =====================================================
    # CREATE PROJECT STRUCTURE
    # =====================================================


    project_path = create_project_structure(

        f"{project_name}_{timestamp}"

    )



    print(
        f"\n[PROJECT CREATED]\n{project_path}"
    )



    # =====================================================
    # WEBSITE TASK
    # =====================================================


    def website_task():


        model = ai_orchestrator.select_model(
            "website"
        )



        print(
            f"\n[WEBSITE MODEL REQUESTED] {model}"
        )



        started = time()



        selected_model = adaptive_router.select_model(

            "WEBSITE",

            model

        )



        print(

            f"[REAL MODEL] {selected_model['model']}"

        )



        result = generate_website(

            prompt=prompt,

            project_path=project_path,

            model=selected_model["model"]

        )



        elapsed = round(

            time() - started,

            2

        )



        performance.add_task(

            "WEBSITE",

            selected_model["model"],

            elapsed

        )



        if progress_callback:

            progress_callback(

                25,

                "WEBSITE COMPLETED"

            )



        return result
    # =====================================================
    # BRANDING TASK
    # =====================================================


    def branding_task():


        model = ai_orchestrator.select_model(
            "branding"
        )



        print(
            f"\n[BRANDING MODEL REQUESTED] {model}"
        )



        started = time()



        selected_model = adaptive_router.select_model(

            "BRANDING",

            model

        )



        print(

            f"[REAL MODEL] {selected_model['model']}"

        )



        result = generate_branding(

            prompt=prompt,

            project_path=project_path,

            model=selected_model["model"]

        )



        elapsed = round(

            time() - started,

            2

        )



        performance.add_task(

            "BRANDING",

            selected_model["model"],

            elapsed

        )



        if progress_callback:


            progress_callback(

                50,

                "BRANDING COMPLETED"

            )



        return result





    # =====================================================
    # SOCIAL TASK
    # =====================================================


    def social_task():


        model = ai_orchestrator.select_model(

            "social"

        )



        print(

            f"\n[SOCIAL MODEL REQUESTED] {model}"

        )



        started = time()



        selected_model = adaptive_router.select_model(

            "SOCIAL",

            model

        )



        print(

            f"[REAL MODEL] {selected_model['model']}"

        )



        result = generate_social(

            prompt=prompt,

            project_path=project_path,

            model=selected_model["model"]

        )



        elapsed = round(

            time() - started,

            2

        )



        performance.add_task(

            "SOCIAL",

            selected_model["model"],

            elapsed

        )



        if progress_callback:


            progress_callback(

                75,

                "SOCIAL COMPLETED"

            )



        return result





    # =====================================================
    # DOCS TASK
    # =====================================================


    def docs_task():


        model = ai_orchestrator.select_model(

            "docs"

        )



        print(

            f"\n[DOCS MODEL REQUESTED] {model}"

        )



        started = time()



        selected_model = adaptive_router.select_model(

            "DOCS",

            model

        )



        print(

            f"[REAL MODEL] {selected_model['model']}"

        )



        result = generate_docs(

            prompt=prompt,

            project_path=project_path,

            model=selected_model["model"]

        )



        elapsed = round(

            time() - started,

            2

        )



        performance.add_task(

            "DOCS",

            selected_model["model"],

            elapsed

        )



        if progress_callback:


            progress_callback(

                90,

                "DOCS COMPLETED"

            )



        return result
    # =====================================================
    # ADD TASKS TO ENGINE
    # =====================================================


    task_engine.add_task(

        "WEBSITE",

        website_task

    )


    task_engine.add_task(

        "BRANDING",

        branding_task

    )


    task_engine.add_task(

        "SOCIAL",

        social_task

    )


    task_engine.add_task(

        "DOCS",

        docs_task

    )



    # =====================================================
    # RUN AUTONOMOUS BUSINESS PIPELINE
    # =====================================================


    task_summary = task_engine.run()



    if progress_callback:


        progress_callback(

            100,

            "BUSINESS TASKS COMPLETED"

        )



    # =====================================================
    # AUTOMATIC VALIDATION
    # =====================================================


    print(

        "\n[AUTOMATIC BUSINESS VALIDATION]"

    )



    validation = validate_project(

        project_path

    )



    print(

        "\n[BUSINESS PROJECT FINISHED]"

    )



    print(

        f"\nOUTPUT PATH:\n{project_path}"

    )



    print(

        "\n[VALIDATION SUMMARY]"

    )



    print(

        f"STATUS: {validation['status']}"

    )



    print(

        f"SCORE: {validation['score']}%"

    )



    print(

        f"APPROVED: "

        f"{validation['approved']}/"

        f"{validation['total_checks']}"

    )



    # =====================================================
    # PERFORMANCE FINAL REPORT
    # =====================================================


    performance.finish()



    print()



    print(

        "[AI PERFORMANCE REPORT]"

    )



    print(

        performance.report()

    )



    # =====================================================
    # FINAL RESPONSE
    # =====================================================


    return {


        "status":

            validation["status"],



        "project":

            str(

                project_path

            ),



        "validation":

            validation,



        "task_summary":

            task_summary

    }
