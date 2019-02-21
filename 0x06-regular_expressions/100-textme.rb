#!/usr/bin/env ruby
scanOne = ARGV[0].scan(/from:(\+?\w+)/)
print scanOne[0].join + ", "
scanTwo = ARGV[0].scan(/to:(\+?\w+)/)
print scanTwo[0].join + ", "
scanThree = ARGV[0].scan(/flags:([-\d:]+)/)
puts scanThree.join
