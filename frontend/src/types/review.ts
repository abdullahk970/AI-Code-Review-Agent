export interface Stats {
  total_reviews: number;
  approvals: number;
  change_requests: number;
}

export interface Review {
  id: number;
  repository: string;
  pr_number: number;
  risk_score: number;
  decision: string;
  summary: string;
}

export interface ReviewIssue {
  category: string;
  severity: string;
  message: string;
  title?: string;
  file_path: string;
  line_number: number;
}

export interface ReviewDetails extends Review {
  issues: ReviewIssue[];
}