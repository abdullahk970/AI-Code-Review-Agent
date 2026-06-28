"use client";

import { useState, useMemo } from "react";
import Link from "next/link";
import { Review } from "@/types/review";
import RiskBadge from "./RiskBadge";

interface Props {
  reviews: Review[];
}

type SortField = "repository" | "pr_number" | "risk_score" | "decision";
type SortOrder = "asc" | "desc";

export default function ReviewTable({ reviews }: Props) {
  const [sortField, setSortField] = useState<SortField>("risk_score");
  const [sortOrder, setSortOrder] = useState<SortOrder>("desc");
  const [searchTerm, setSearchTerm] = useState("");

  const filteredAndSortedReviews = useMemo(() => {
    let result = [...reviews];

    // Filter by search term
    if (searchTerm) {
      result = result.filter(
        (review) =>
          review.repository
            .toLowerCase()
            .includes(searchTerm.toLowerCase()) ||
          review.pr_number.toString().includes(searchTerm)
      );
    }

    // Sort
    result.sort((a, b) => {
      let aValue = a[sortField];
      let bValue = b[sortField];

      // Handle numeric sorting
      if (typeof aValue === "number" && typeof bValue === "number") {
        return sortOrder === "asc" ? aValue - bValue : bValue - aValue;
      }

      // Handle string sorting
      if (typeof aValue === "string" && typeof bValue === "string") {
        return sortOrder === "asc"
          ? aValue.localeCompare(bValue)
          : bValue.localeCompare(aValue);
      }

      return 0;
    });

    return result;
  }, [reviews, sortField, sortOrder, searchTerm]);

  const handleSort = (field: SortField) => {
    if (sortField === field) {
      setSortOrder(sortOrder === "asc" ? "desc" : "asc");
    } else {
      setSortField(field);
      setSortOrder("desc");
    }
  };

  const SortIcon = ({ field }: { field: SortField }) => {
    if (sortField !== field) {
      return (
        <svg
          className="w-4 h-4 text-gray-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M7 16V4m0 0L3 8m0 0l4 4m10-4v12m0 0l4-4m0 0l-4-4"
          />
        </svg>
      );
    }

    return (
      <svg
        className={`w-4 h-4 transition-transform ${
          sortOrder === "desc" ? "rotate-180" : ""
        }`}
        fill="currentColor"
        viewBox="0 0 24 24"
      >
        <path d="M7 15l5-5 5 5" />
      </svg>
    );
  };

  return (
    <div className="space-y-4">
      <div className="relative">
        <input
          type="text"
          placeholder="Search by repository or PR number..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {searchTerm && (
          <button
            onClick={() => setSearchTerm("")}
            className="absolute right-3 top-2.5 text-gray-400 hover:text-gray-600"
          >
            ✕
          </button>
        )}
      </div>

      <div className="overflow-x-auto rounded-lg border border-gray-200">
        <table className="w-full">
          <thead className="bg-gray-100 border-b">
            <tr>
              <th className="p-3 text-left">
                <button
                  onClick={() => handleSort("repository")}
                  className="flex items-center space-x-1 hover:text-blue-600"
                >
                  <span className="font-semibold">Repository</span>
                  <SortIcon field="repository" />
                </button>
              </th>
              <th className="p-3 text-left">
                <button
                  onClick={() => handleSort("pr_number")}
                  className="flex items-center space-x-1 hover:text-blue-600"
                >
                  <span className="font-semibold">PR</span>
                  <SortIcon field="pr_number" />
                </button>
              </th>
              <th className="p-3 text-left">
                <button
                  onClick={() => handleSort("risk_score")}
                  className="flex items-center space-x-1 hover:text-blue-600"
                >
                  <span className="font-semibold">Risk & Decision</span>
                  <SortIcon field="risk_score" />
                </button>
              </th>
              <th className="p-3 text-left">
                <span className="font-semibold">Action</span>
              </th>
            </tr>
          </thead>
          <tbody>
            {filteredAndSortedReviews.length > 0 ? (
              filteredAndSortedReviews.map((review) => (
                <tr
                  key={review.id}
                  className="border-t hover:bg-blue-50 transition-colors"
                >
                  <td className="p-3">
                    <span className="font-medium text-gray-900">
                      {review.repository}
                    </span>
                  </td>
                  <td className="p-3">
                    <span className="text-gray-600">#{review.pr_number}</span>
                  </td>
                  <td className="p-3">
                    <RiskBadge
                      riskScore={review.risk_score}
                      decision={review.decision}
                    />
                  </td>
                  <td className="p-3">
                    <Link
                      href={`/reviews/${review.id}`}
                      className="inline-flex items-center space-x-1 text-blue-600 hover:text-blue-800 hover:underline"
                    >
                      <span>View Details</span>
                      <svg
                        className="w-4 h-4"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M9 5l7 7-7 7"
                        />
                      </svg>
                    </Link>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={4} className="p-8 text-center text-gray-500">
                  No reviews match your search
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {filteredAndSortedReviews.length > 0 && (
        <div className="text-sm text-gray-600 text-right">
          Showing {filteredAndSortedReviews.length} of {reviews.length} reviews
        </div>
      )}
    </div>
  );
}
