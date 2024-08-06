import styles from './header.module.scss'

export const Header = () => {
  return (
    <div className={styles.banner}>
      <div className={styles.container}>
        <h2 className="logo-font">Map of spotify</h2>
        <p>Graph clustering.</p>
      </div>
    </div>
  )
}