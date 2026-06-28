from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.services.database_service import DatabaseService
from app.services.report_service import ReportService

router = APIRouter(
    tags=["Report"]
)


@router.get("/report/{review_id}")
def generate_report(review_id: int):

    database = DatabaseService()

    review = database.get_review(review_id)

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    report_service = ReportService()

    pdf_path = report_service.generate_report(review)

    if not Path(pdf_path).exists():
        raise HTTPException(
            status_code=500,
            detail="Failed to generate report."
        )

    return FileResponse(
        path=pdf_path,
        filename=pdf_path.name,
        media_type="application/pdf"
    )