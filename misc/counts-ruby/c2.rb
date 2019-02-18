#! /usr/bin/env ruby
# require 'stackprof'

hexagons = pentagons = []
hexagons  = ((4..12).to_a * 6).map{|n|6*n}
pentagons = ((5..12).to_a * 4).map{|n|5*n}
all = hexagons + pentagons - [50]
size = all.size
# all = [24, 24, 24, 24, 25, 25, 30, 30, 30, 30, 30, 30, 30, 35, 35, 36, 40]
c = 0

l = 69
loss = 0

# StackProf.run(mode: :object, raw: true, out: 'counts.dump') do
#   while c< 100
  while true
    s = all.shuffle
    (0...(size-l)).each do |i|
      ((i+l)...size).each do |j|
        strips = s[i..j]
        total = strips.sum
        count = strips.length
        if count * 50 <= total + loss && total % 50 == 0
          puts "i: #{i} j: #{j}\n#{count} strings (#{total} vs #{count*50})\n#{strips.sort}"
        end

        c+=1
        puts c if c % 10_000_000 == 0
      end
    end
  end
# end
