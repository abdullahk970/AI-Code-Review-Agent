"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { getReviewDetails } from "@/lib/api";
import IssueList from "@/components/IssueList";
import RiskBadge from "@/components/RiskBadge";
import LoadingSpinner from "@/components/LoadingSpinner";
import ErrorDisplay from "@/components/ErrorDisplay";
import { ReviewDetails } from "@/types/review";

interface Props {
  params: Promise<{ id: string }>;
}

export default function ReviewPage({ params }: Props) {
  const [review, setReview] = useState<ReviewDetails | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [id, setId] = useState<string | null>(null);

  useEffect(() => {
    const loadParams = async () => {
      try {
        const { id: reviewId } = await params;
        setId(reviewId);

        const reviewData = await getReviewDetails(Number(reviewId));
        setReview(reviewData);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : "Failed to load review details"
        );
      } finally {
        setLoading(false);
      }
    };

    loadParams();
  }, [params]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <LoadingSpinner />
      </div>
    );
  }

  if (error || !review) {
    return <ErrorDisplay message={error || "Review not found"} />;
  }

  return (
    <main className="max-w-5xl mx-auto p-8">
      {/* Back Button */}
      <Link
        href="/"
        className="inline-flex items-center space-x-1 text-blue-600 hover:text-blue-800 mb-6"
      >
        <svg
          className="w-5 h-5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M15 19l-7-7 7-7"
          />
        </svg>
        <span>Back to Dashboard</span>
      </Link>

      {/* Header */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2">Review #{review.id}</h1>
        <p className="text-gray-600">
          {new Date().toLocaleDateString()} • {review.repository}
        </p>
      </div>

      {/* Status Overview */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        {/* Main Details */}
        <div className="border border-gray-200 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4">Review Details</h2>
          <div className="space-y-4">
            <div>
              <p className="text-sm text-gray-600">Repository</p>
              <p className="text-lg font-medium">{review.repository}</p>
            </div>
            <div>
              <p className="text-sm text-gray-600">Pull Request</p>
              <p className="text-lg font-medium">#{review.pr_number}</p>
            </div>
            <div>
              <p className="text-sm text-gray-600">Summary</p>
              <p className="text-base mt-1">{review.summary}</p>
            </div>
          </div>
        </div>

        {/* Risk Assessment */}
        <div className="border border-gray-200 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4">Risk Assessment</h2>
          <div className="space-y-4">
            <div>
              <p className="text-sm text-gray-600 mb-2">Status & Risk Level</p>
              <div className="flex items-center">
                <RiskBadge
                  riskScore={review.risk_score}
                  decision={review.decision}
                />
              </div>
            </div>
            <div>
              <p className="text-sm text-gray-600">Risk Score</p>
              <div className="mt-2 w-full bg-gray-200 rounded-full h-3">
                <div
                  className={`h-3 rounded-full transition-all ${
                    review.risk_score <= 20
                      ? "bg-green-500"
                      : review.risk_score <= 50
                        ? "bg-yellow-500"
                        : review.risk_score <= 80
                          ? "bg-orange-500"
                          : "bg-red-500"
                  }`}
                  style={{ width: `${review.risk_score}%` }}
                />
              </div>
              <p className="text-sm text-gray-600 mt-2">
                {review.risk_score}%
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Issues */}
      <div className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">
          Issues Found ({review.issues?.length || 0})
        </h2>
        <IssueList issues={review.issues || []} />
      </div>

      {/* Action Footer */}
      <div className="border-t pt-6 flex justify-between items-center">
        <Link
          href="/"
          className="text-blue-600 hover:text-blue-800 font-medium"
        >
          ← Back to Dashboard
        </Link>
        <button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition" >
          Generate Report
        </button>
      </div>
    </main>
  );
}
