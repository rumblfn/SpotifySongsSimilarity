import { FC, ReactNode } from 'react'
import { ErrorBoundary } from 'react-error-boundary'
import { Fallback } from 'shared/ui/fallback'

interface IProviders {
  /** Content that will be wrapped by providers. */
  readonly children: ReactNode
}

export const Providers: FC<IProviders> = ({ children }) => {
  return (
    <ErrorBoundary FallbackComponent={Fallback}>
      {children}
    </ErrorBoundary>
  )
}