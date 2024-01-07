#!/usr/bin/env ruby

def match_school(input)
  regex = /hbt*?n/

  matches = input.scan(regex)

  unless matches.empty?
    puts "#{matches.join('')}"
  end
end

input_arg = ARGV[0]

if input_arg.nil?
  puts "Please provide an argument."
else
  match_school(input_arg)
end
