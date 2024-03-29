def fizzBuzz(n)
  result = []

  (1..n).each do |i|

    add = ''

    if i %3 == 0
      add += 'Fizz'
    end

    if i % 5 == 0
      add += 'Buzz'
    end

    if add == ''
      result.push(i)
    else
      result.push(add)
    end
  end
  return result
end
