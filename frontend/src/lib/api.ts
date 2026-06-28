import { Review, ReviewDetails, ReviewIssue, Stats } from "@/types/review";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

interface BackendStats {
  total_reviews?: number;
  approvals?: number;
  change_requests?: number;
}

interface BackendReviewResponse {
  id: number;
  repository: string;
  pr_number: number;
  risk_score: number;
  decision: string;
  // summary can be either a structured object or a plain string
  summary?:
    | string
    | {
        total_bugs: number;
        total_security_issues: number;
        total_performance_issues: number;
        total_style_issues: number;
        total_issues: number;
      };
}

interface BackendReviewDetailsResponse extends BackendReviewResponse {
  status?: string;
  // summary can be either a structured object or a plain string
  summary?:
    | {
        total_bugs: number;
        total_security_issues: number;
        total_performance_issues: number;
        total_style_issues: number;
        total_issues: number;
      }
    | string;
  review?: {
    bugs?: Array<{ title?: string; description?: string; line?: number }>;
    security?: Array<{
      title?: string;
      description?: string;
      line?: number;
    }>;
    performance?: Array<{
      title?: string;
      issue?: string;
      description?: string;
      location?: string;
    }>;
    style?: Array<{
      title?: string;
      issue?: string;
      description?: string;
      location?: string;
    }>;
  };
  analysis?: {
    risk_score: number;
    decision: string;
  };
}

// Transform backend review issues to frontend format
function transformIssues(
  backendReview?: BackendReviewDetailsResponse["review"]
): ReviewIssue[] {
  if (!backendReview) return [];

  const issues: ReviewIssue[] = [];

  // Process bugs
  if (backendReview.bugs) {
    backendReview.bugs.forEach((bug) => {
      issues.push({
        category: "bugs",
        severity: "HIGH",
        message: bug.description || bug.title || "",
        title: bug.title,
        file_path: "",
        line_number: bug.line || 0,
      });
    });
  }

  // Process security issues
  if (backendReview.security) {
    backendReview.security.forEach((sec) => {
      issues.push({
        category: "security",
        severity: "CRITICAL",
        message: sec.description || sec.title || "",
        title: sec.title,
        file_path: "",
        line_number: sec.line || 0,
      });
    });
  }

  // Process performance issues
  if (backendReview.performance) {
    backendReview.performance.forEach((perf) => {
      issues.push({
        category: "performance",
        severity: "MEDIUM",
        message: perf.description || perf.issue || "",
        title: perf.title,
        file_path: perf.location || "",
        line_number: 0,
      });
    });
  }

  // Process style issues
  if (backendReview.style) {
    backendReview.style.forEach((style) => {
      issues.push({
        category: "style",
        severity: "LOW",
        message: style.description || style.issue || "",
        title: style.title,
        file_path: style.location || "",
        line_number: 0,
      });
    });
  }

  return issues;
}

export async function getStats(): Promise<Stats> {
  try {
    const res = await fetch(`${API_URL}/stats`, {
      cache: "no-store",
    });

    if (!res.ok) throw new Error("Stats API failed");

    const data: BackendStats = await res.json();

    return {
      total_reviews: data.total_reviews || 0,
      approvals: data.approvals || 0,
      change_requests: data.change_requests || 0,
    };
  } catch (err) {
    console.error("Failed to fetch stats:", err);
    return {
      total_reviews: 0,
      approvals: 0,
      change_requests: 0,
    };
  }
}

export async function getReviews(): Promise<Review[]> {
  try {
    const res = await fetch(`${API_URL}/reviews`, {
      cache: "no-store",
    });

    if (!res.ok) throw new Error("Reviews API failed");

    const data: BackendReviewResponse[] = await res.json();

    return data.map((review) => ({
      id: review.id,
      repository: review.repository,
      pr_number: review.pr_number,
      risk_score: review.risk_score,
      decision: review.decision,
      summary:
        typeof review.summary === "string"
          ? review.summary
          : review.summary
            ? `Found ${review.summary.total_issues} issues`
            : "",
    }));
  } catch (err) {
    console.error("Failed to fetch reviews:", err);
    return [];
  }
}

export async function getReviewDetails(id: number): Promise<ReviewDetails> {
  try {
    const res = await fetch(`${API_URL}/review-details/${id}`, {
      cache: "no-store",
    });

    if (!res.ok) throw new Error("Review details API failed");

    const data: BackendReviewDetailsResponse = await res.json();

    // Transform backend response to frontend types
    const riskScore = data.analysis?.risk_score || data.risk_score || 0;
    const decision = data.analysis?.decision || data.decision || "UNKNOWN";

    return {
      id: data.id,
      repository: data.repository,
      pr_number: data.pr_number,
      risk_score: riskScore,
      decision,
      summary:
        data.summary && typeof data.summary === "object"
          ? `Found ${data.summary.total_issues} issues across ${Object.keys(data.review || {}).length} categories`
          : data.summary || "Review in progress",
      issues: transformIssues(data.review),
    };
  } catch (err) {
    console.error("Failed to fetch review details:", err);
    return {
      id,
      repository: "Unknown Repository",
      pr_number: 0,
      risk_score: 0,
      decision: "UNKNOWN",
      summary: "Unable to load review details. Please try again.",
      issues: [],
    };
  }
}