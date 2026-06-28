"use client";

import { useMemo } from "react";
import { ReviewIssue } from "@/types/review";

interface Props {
  issues: ReviewIssue[];
}

const categoryColors: Record<
  string,
  { bg: string; text: string; icon: string }
> = {
  bugs: {
    bg: "bg-red-50",
    text: "text-red-700",
    icon: "🐛",
  },
  security: {
    bg: "bg-orange-50",
    text: "text-orange-700",
    icon: "🔒",
  },
  performance: {
    bg: "bg-blue-50",
    text: "text-blue-700",
    icon: "⚡",
  },
  style: {
    bg: "bg-purple-50",
    text: "text-purple-700",
    icon: "✨",
  },
};

const severityColors: Record<string, string> = {
  CRITICAL: "text-red-600 font-bold",
  HIGH: "text-red-500 font-semibold",
  MEDIUM: "text-yellow-600 font-semibold",
  LOW: "text-green-600 font-semibold",
};

export default function IssueList({ issues }: Props) {
  const groupedIssues = useMemo(() => {
    return issues.reduce(
      (acc, issue) => {
        const category = issue.category.toLowerCase();
        if (!acc[category]) {
          acc[category] = [];
        }
        acc[category].push(issue);
        return acc;
      },
      {} as Record<string, ReviewIssue[]>
    );
  }, [issues]);

  if (!issues.length) {
    return (
      <div className="text-center py-8 border rounded-lg bg-green-50">
        <p className="text-green-700 font-semibold">✓ No issues found!</p>
        <p className="text-green-600 text-sm mt-1">
          Your code looks good to go.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {Object.entries(groupedIssues).map(([category, categoryIssues]) => {
        const colors = categoryColors[category] || categoryColors.bugs;
        return (
          <div key={category}>
            <div className="flex items-center space-x-2 mb-3">
              <span className="text-2xl">{colors.icon}</span>
              <h3 className={`text-lg font-semibold ${colors.text}`}>
                {category.charAt(0).toUpperCase() + category.slice(1)} Issues
                <span className="ml-2 text-sm font-normal text-gray-600">
                  ({categoryIssues.length})
                </span>
              </h3>
            </div>

            <div className={`space-y-3 p-4 rounded-lg ${colors.bg}`}>
              {categoryIssues.map((issue, index) => (
                <div
                  key={index}
                  className="bg-white rounded p-4 border border-gray-200"
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      {issue.title ? (
                        <h4 className="font-semibold text-gray-900">
                          {issue.title}
                        </h4>
                      ) : null}
                      <p className="mt-1 text-gray-700">{issue.message}</p>

                      <div className="mt-3 flex flex-wrap gap-3 text-sm">
                        {issue.file_path && (
                          <span className="text-gray-600">
                            📄 {issue.file_path}
                          </span>
                        )}
                        {issue.line_number && (
                          <span className="text-gray-600">
                            Line {issue.line_number}
                          </span>
                        )}
                      </div>
                    </div>

                    <div className="ml-4 flex-shrink-0">
                      <span
                        className={`inline-block px-3 py-1 rounded-full text-xs font-medium ${
                          severityColors[issue.severity] ||
                          severityColors.LOW
                        }`}
                      >
                        {issue.severity || "INFO"}
                      </span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}
