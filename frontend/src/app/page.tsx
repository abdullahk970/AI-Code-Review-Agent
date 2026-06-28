"use client";

import { Suspense, useState, useEffect } from "react";
import { getStats, getReviews } from "@/lib/api";
import StatsCards from "@/components/StatsCards";
import ReviewTable from "@/components/ReviewTable";
import LoadingSpinner from "@/components/LoadingSpinner";
import ErrorDisplay from "@/components/ErrorDisplay";
import { Stats, Review } from "@/types/review";

function DashboardContent() {
  const [stats, setStats] = useState<Stats | null>(null);
  const [reviews, setReviews] = useState<Review[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        setError(null);

        const [statsData, reviewsData] = await Promise.all([
          getStats(),
          getReviews(),
        ]);

        setStats(statsData);
        setReviews(reviewsData);
      } catch (err) {
        setError(
          err instanceof Error
            ? err.message
            : "Failed to load dashboard data"
        );
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <LoadingSpinner />
      </div>
    );
  }

  if (error) {
    return <ErrorDisplay message={error} />;
  }

  return (
    <main className="max-w-7xl mx-auto p-8">
      <h1 className="text-4xl font-bold mb-2">AI Code Review Dashboard</h1>
      <p className="text-gray-600 mb-8">
        Monitor and manage your code review pipeline
      </p>

      {stats && <StatsCards {...stats} />}

      <h2 className="text-2xl font-semibold mb-4 mt-8">Recent Reviews</h2>

      {reviews.length > 0 ? (
        <ReviewTable reviews={reviews} />
      ) : (
        <div className="text-center py-8 border rounded-lg bg-gray-50">
          <p className="text-gray-600">No reviews found. Start by pushing code!</p>
        </div>
      )}
    </main>
  );
}

export default function Home() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <DashboardContent />
    </Suspense>
  );
}
