/// <reference types="vite-plugin-svgr/client" />

import {Link, useRouteError} from 'react-router-dom'
import ErrorImage from 'shared/assets/images/errorImage.svg?react'
import {RejectedDataType} from 'shared/types';

import styles from './fallback.module.scss'

export const Fallback = () => {
  const error = useRouteError()
  const knownError = error as RejectedDataType

  return (
    <div role='alert' className={styles.fallback}>
      <ErrorImage className={styles.fallback__img}/>
      <h1 className={styles.fallback__img}>Something went wrong</h1>
      <span className={styles.fallback__describe}>
                {knownError?.messageError} {knownError?.status}
            </span>
      <Link to='/' className={styles.fallback__link}>
        Go to home page
      </Link>
    </div>
  )
}