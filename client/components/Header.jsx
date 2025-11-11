import styles from './Hero/Hero.module.css'
import { useRouter} from 'next/router'
import Link from 'next/link'

/**
 * A component that displays the main header of the application.
 *
 * The header includes the site title, a search bar, navigation links,
 * and a "Buy Tickets" button. It is hidden on the login and signup pages.
 *
 * @returns {JSX.Element} The rendered header component.
 */
const Header = () => {
  const router = useRouter()
  return (
    <header style={{ display: router.pathname === "/auth/login" || router.pathname === "/auth/signup" ? 'none' : 'flex' }} className={styles.header}>
      <div><h1>Get-Ticketz</h1></div>
      <div>
        <ul>
          <li><input placeholder='Search Event....' type="search" name="" id="" /></li>
          <li>Organize</li>
          <li>Create Event</li>
          <li>Agenda</li>
          <Link href={`/auth/login`}><li>Log in</li></Link>
          <Link href={`/auth/signup`}><li>Sign up</li></Link>
        </ul>
      </div>
      <div className={styles.ticks}>
        <div></div>
        <div>Buy Tickets</div>
      </div>
    </header>
  )
}

export default Header