/** Type of error sent to the storage. */
export interface RejectedDataType {
  /** Error message.  */
  readonly messageError: string
  /** Error status. */
  readonly status?: string
}
