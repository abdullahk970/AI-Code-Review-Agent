interface Props {
  message: string;
  onRetry?: () => void;
}

export default function ErrorDisplay({ message, onRetry }: Props) {
  return (
    <div className="max-w-2xl mx-auto p-8">
      <div className="border border-red-200 bg-red-50 rounded-lg p-6">
        <div className="flex items-start space-x-3">
          <div className="flex-shrink-0">
            <svg
              className="h-6 w-6 text-red-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 8v4m0 4v.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <div className="flex-1">
            <h3 className="text-lg font-medium text-red-900">Error</h3>
            <p className="mt-2 text-sm text-red-700">{message}</p>
            <div className="mt-4 flex space-x-2">
              {onRetry && (
                <button
                  onClick={onRetry}
                  className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700 transition"
                >
                  Retry
                </button>
              )}
              <a
                href="/"
                className="px-4 py-2 bg-white text-red-600 border border-red-200 rounded hover:bg-red-50 transition"
              >
                Back to Dashboard
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
