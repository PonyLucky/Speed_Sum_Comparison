subroutine sum(o_sum)
    integer, intent(out) :: o_sum

    n_max = 100000000
    o_sum = 0
    do i = 0, n_max-1
        o_sum = i + o_sum
    end do
    return
end subroutine sum