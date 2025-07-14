
The following content is provided under a Creative Commons license.

Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free.

To make a donation or to view additional materials from hundreds of MIT courses visit MIT OpenCourseWare at ocw.mit.edu.

Okay so I'd like to begin the second lecture by reminding you what we did last time.

So last time, we defined the derivative as the slope of a tangent line.

So that was our geometric point of view and we also did a couple of computations.

We worked out that the derivative of 1 / x was -1 / x^2.

And we also computed the derivative of x to the nth power for n = 1, 2, etc., and that turned out to be x, I'm sorry, nx^(n-1).

So that's what we did last time, and today I want to finish up with other points of view on what a derivative is.

So this is extremely important, it's almost the most important thing I'll be saying in the class.

But you'll have to think about it again when you start over and start using calculus in the real world.

So again we're talking about what is a derivative and this is just a continuation of last time.

So, as I said last time, we talked about geometric interpretations, and today what we're gonna talk about is rate of change as an interpretation of the derivative.

So remember we drew graphs of functions, y = f(x) and we kept track of the change in x and here the change in y, let's say.

And then from this new point of view a rate of change, keeping track of the rate of change of x and the rate of change of y, it's the relative rate of change we're interested in, and that's delta y / delta x and that has another interpretation.

This is the average change.

Usually we would think of that, if x were measuring time and so the average and that's when this becomes a rate, and the average is over the time interval delta x.

And then the limiting value is denoted dy/dx and so this one is the average rate of change and this one is the instantaneous rate.

Okay, so that's the point of view that I'd like to discuss now and give you just a couple of examples.

So, let's see.

Well, first of all, maybe some examples from physics here.

So q is usually the name for a charge, and then dq/dt is what's known as current.

So that's one physical example.

A second example, which is probably the most tangible one, is we could denote the letter s by distance and then the rate of change is what we call speed.

So those are the two typical examples and I just want to illustrate the second example in a little bit more detail because I think it's important to have some visceral sense of this notion of instantaneous speed.

And I get to use the example of this very building to do that.

Probably you know, or maybe you don't, that on Halloween there's an event that takes place in this building or really from the top of this building which is called the pumpkin drop.

So let's illustrates this idea of rate of change with the pumpkin drop.

So what happens is, this building-- well let's see here's the building, and here's the dot, that's the beautiful grass out on this side of the building, and then there's some people up here and very small objects, well they're not that small when you're close to them, that get dumped over the side there.

And they fall down.

You know everything at MIT or a lot of things at MIT are physics experiments.

That's the pumpkin drop.

So roughly speaking, the building is about 300 feet high, we're down here on the first usable floor.

And so we're going to use instead of 300 feet, just for convenience purposes we'll use 80 meters because that makes the numbers come out simply.

So we have the height which starts out at 80 meters at time 0 and then the acceleration due to gravity gives you this formula for h, this is the height.

So at time t = 0, we're up at the top, h is 80 meters, the units here are meters.

And at time t = 4 you notice, 5 * 4^2 is 80.

I picked these numbers conveniently so that we're down at the bottom.

Okay, so this notion of average change here, so the average change, or the average speed here, maybe we'll call it the average speed, since that's-- over this time that it takes for the pumpkin to drop is going to be the change in h divided by the change in t.

Which starts out at, what does it start out as?

It starts out as 80, right?

And it ends at 0.

So actually we have to do it backwards.

We have to take 0 - 80 because the first value is the final position and the second value is the initial position.

And that's divided by 4 - 0; times 4 seconds minus times 0 seconds.

And so that of course is -20 meters per second.

So the average speed of this guy is 20 meters a second.

Now, so why did I pick this example?

Because, of course, the average, although interesting, is not really what anybody cares about who actually goes to the event.

All we really care about is the instantaneous speed when it hits the pavement and so that's can be calculated at the bottom.

So what's the instantaneous speed?

That's the derivative, or maybe to be consistent with the notation I've been using so far, that's d/dt of h.

All right?

So that's d/dt of h.

Now remember we have formulas for these things.

We can differentiate this function now.

We did that yesterday.

So we're gonna take the rate of change and if you take a look at it, it's just the rate of change of 80 is 0, minus the rate change for this -5t^2, that's minus 10t.

So that's using the fact that d/dt of 80 is equal to 0 and d/dt of t^2 is equal to 2t.

The special case...

Well I'm cheating here, but there's a special case that's obvious.

I didn't throw it in over here.

The case n = 2 is that second case there.

But the case n = 0 also works.

Because that's constants.

The derivative of a constant is 0.

And then the factor n there's 0 and that's consistent.

And actually if you look at the formula above it you'll see that it's the case of n = -1.

So we'll get a larger pattern soon enough with the powers.

Okay anyway.

Back over here we have our rate of change and this is what it is.

And at the bottom, at that point of impact, we have t = 4 and so h', which is the derivative, is equal to -40 meters per second.

So twice as fast as the average speed here, and if you need to convert that, that's about 90 miles an hour.

Which is why the police are there at midnight on Halloween to make sure you're all safe and also why when you come you have to be prepared to clean up afterwards.

So anyway that's what happens, it's 90 miles an hour.

It's actually the buildings a little taller, there's air resistance and I'm sure you can do a much more thorough study of this example.

All right so now I want to give you a couple of more examples because time and these kinds of parameters and variables are not the only ones that are important for calculus.

If it were only this kind of physics that was involved, then this would be a much more specialized subject than it is.

And so I want to give you a couple of examples that don't involve time as a variable.

So the third example I'll give here is-- The letter T often denotes temperature, and then dT/dx would be what is known as the temperature gradient.

Which we really care about a lot when we're predicting the weather because it's that temperature difference that causes air flows and causes things to change.

And then there's another theme which is throughout the sciences and engineering which I'm going to talk about under the heading of sensitivity of measurements.

So let me explain this.

I don't want to belabor it because I just am doing this in order to introduce you to the ideas on your problem set which are the first case of this.

So on problem set one you have an example which is based on a simplified model of GPS, sort of the Flat Earth Model.

And in that situation, well, if the Earth is flat it's just a horizontal line like this.

And then you have a satellite, which is over here, preferably above the earth, and the satellite or the system knows exactly where the point directly below the satellite is.

So this point is treated as known.

And I'm sitting here with my little GPS device and I want to know where I am.

And the way I locate where I am is I communicate with this satellite by radio signals and I can measure this distance here which is called h.

And then system will compute this horizontal distance which is L.

So in other words what is measured, so h measured by radios, radio waves and a clock, or various clocks.

And then L is deduced from h.

And what's critical in all of these systems is that you don't know h exactly.

There's an error in h which will denote delta h.

There's some degree of uncertainty.

The main uncertainty in GPS is from the ionosphere.

But there are lots of corrections that are made of all kinds.

And also if you're inside a building it's a problem to measure it.

But it's an extremely important issue, as I'll explain in a second.

So the idea is we then get at delta L is estimated by considering this ratio delta L/delta h which is going to be approximately the same as the derivative of L with respect to h.

So this is the thing that's easy because of course it's calculus.

Calculus is the easy part and that allows us to deduce something about the real world that's close by over here.

So the reason why you should care about this quite a bit is that it's used all the time to land airplanes.

So you really do care that they actually know to within a few feet or even closer where your plane is and how high up it is and so forth.

All right.

So that's it for the general introduction of what a derivative is.

I'm sure you'll be getting used to this in a lot of different contexts throughout the course.

And now we have to get back down to some rigorous details.

Okay, everybody happy with what we've got so far?

Yeah?

Student: [INAUDIBLE]

Professor: Ah good question.

The question was how did I get this equation for height?

I just made it up because it's the formula from physics that you will learn when you take 8.01 and, in fact, it has to do with the fact that this is the speed if you differentiate another time you get acceleration and acceleration due to gravity is 10 meters per second.

Which happens to be the second derivative of this.

But anyway I just pulled it out of a hat from your physics class.

So you can just say see 8.01 .

All right, other questions?

All right, so let's go on now.

Now I have to be a little bit more systematic about limits.

So let's do that now.

So now what I'd like to talk about is limits and continuity.

And this is a warm up for deriving all the rest of the formulas, all the rest of the formulas that I'm going to need to differentiate every function you know.

Remember, that's our goal and we only have about a week left so we'd better get started.

So first of all there is what I will call easy limits.

So what's an easy limit?

An easy limit is something like the limit as x goes to 4 of x plus 3 over x^2 + 1.

And with this kind of limit all I have to do to evaluate it is to plug in x = 4 because, so what I get here is 4 + 3 divided by 4^2 + 1.

And that's just 7 / 17.

And that's the end of it.

So those are the easy limits.

The second kind of limit - well so this isn't the only second kind of limit but I just want to point this out, it's very important - is that: derivatives are are always harder than this.

You can't get away with nothing here.

So, why is that?

Well, when you take a derivative, you're taking the limit as x goes to x_0 of f(x), well we'll write it all out in all its glory.

Here's the formula for the derivative.

Now notice that if you plug in x = x:0, always gives 0 / 0.

So it just basically never works.

So we always are going to need some cancellation to make sense out of the limit.

Now in order to make things a little easier for myself to explain what's going on with limits I need to introduce just one more piece of notation.

What I'm gonna introduce here is what's known as a left-hand and a right limit.

If I take the limit as x tends to x_0 with a plus sign here of some function, this is what's known as the right-hand limit.

And I can display it visually.

So what does this mean?

It means practically the same thing as x tends to x_0 except there is one more restriction which has to do with this plus sign, which is we're going from the plus side of x_0.

That means x is bigger than x_0.

And I say right-hand, so there should be a hyphen here, right-hand limit because on the number line, if x_0 is over here the x is to the right.

All right?

So that's the right-hand limit.

And then this being the left side of the board, I'll put on the right side of the board the left limit, just to make things confusing.

So that one has the minus sign here.

I'm just a little dyslexic and I hope you're not.

So I may have gotten that wrong.

So this is the left-hand limit, and I'll draw it.

So of course that just means x goes to x_0 but x is to the left of x_0 .

And again, on the number line, here's the x_0 and the x is on the other side of it.

Okay, so those two notations are going to help us to clarify a bunch of things.

It's much more convenient to have this extra bit of description of limits than to just consider limits from both sides.

Okay so I want to give an example of this.

And also an example of how you're going to think about these sorts of problems.

So I'll take a function which has two different definitions.

Say it's x + 1, when x > 0 and -x + 2, when x < 0.

So maybe put commas there.

So when x > 0, it's x + 1.

Now I can draw a picture of this.

It's gonna be kind of a little small because I'm gonna try to fit it down in here, but maybe I'll put the axis down below.

So at height 1, I have to the right something of slope 1 so it goes up like this.

All right?

And then to the left of 0 I have something which has slope -1, but it hits the axis at 2 so it's up here.

So I had this sort of strange antenna figure here, which is my graph.

Maybe I should draw these in another color to depict that.

And then if I calculate these two limits here, what I see is that the limit as x goes to 0 from above of f(x), that's the same as the limit as x goes to 0 of the formula here, x + 1.

Which turns out to be 1.

And if I take the limit, so that's the left-hand limit.

Sorry, I told you I was dyslexic.

This is the right, so it's that right-hand.

Here we go.

So now I'm going from the left, and it's f(x) again, but now because I'm on that side the thing I need to plug is the other formula, -x + 2, and that's gonna give us 2.

Now, notice that the left and right limits, and this is one little tiny subtlety and it's almost the only thing that I need you to really pay attention to a little bit right now, is that this, we did not need x = 0 value.

In fact I never even told you what f(0) was here.

If we stick it in we could stick it in.

Okay let's say we stick it in on this side.

Let's make it be that it's on this side.

So that means that this point is in and this point is out.

So that's a typical notation: this little open circle and this closed dot for when you include the.

So in that case the value of f(x) happens to be the same as its right-hand limit, namely the value is 1 here and not 2.

Okay, so that's the first kind of example.

Questions?

Okay, so now our next job is to introduce the definition of continuity.

So that was the other topic here.

So we're going to define.

So f is continuous at x_0 means that the limit of f(x) as x tends to x_0 is equal to f(x_0) .

Right?

So the reason why I spend all this time paying attention to the left and the right and so on and so forth and focusing is that I want you to pay attention for one moment to what the content of this definition is.

What it's saying is the following: continuous at x_0 has various ingredients here.

So the first one is that this limit exists.

And what that means is that there's an honest limiting value both from the left and right.

And they also have to be the same.

All right, so that's what's going on here.

And the second property is that f(x_0) is defined.

So I can't be in one of these situations where I haven't even specified what f(x_0) is and they're equal.

Okay, so that's the situation.

Now again let me emphasize a tricky part of the definition of a limit.

This side, the left-hand side is completely independent, is evaluated by a procedure which does not involve the right-hand side.

These are separate things.

This one is, to evaluate it, you always avoid the limit point.

So that's if you like a paradox, because it's exactly the question: is it true that if you plug in x_0 you get the same answer as if you move in the limit?

That's the issue that we're considering here.

We have to make that distinction in order to say that these are two, otherwise this is just tautological.

It doesn't have any meaning.

But in fact it does have a meaning because one thing is evaluated separately with reference to all the other points and the other is evaluated right at the point in question.

And indeed what these things are, are exactly the easy limits.

That's exactly what we're talking about here.

They're the ones you can evaluate this way.

So we have to make the distinction.

And these other ones are gonna be the ones which we can't evaluate that way.

So these are the nice ones and that's why we care about them, why we have a whole definition associated with them.

All right?

So now what's next?

Well, I need to give you a a little tour, very brief tour, of the zoo of what are known as discontinuous functions.

So sort of everything else that's not continuous.

So, the first example here, let me just write it down here.

It's jump discontinuities.

So what would a jump discontinuity be?

Well we've actually already seen it.

The jump discontinuity is the example that we had right there.

This is when the limit from the left and right exist, but are not equal.

Okay, so that's as in the example.

Right?

In this example, the two limits, one of them was 1 and of them was 2.

So that's a jump discontinuity.

And this kind of issue, of whether something is continuous or not, may seem a little bit technical but it is true that people have worried about it a lot.

Bob Merton, who was a professor at MIT when he did his work for the Nobel prize in economics, was interested in this very issue of whether stock prices of various kinds are continuous from the left or right in a certain model.

And that was a very serious issue in developing the model that priced things that our hedge funds use all the time now.

So left and right can really mean something very different.

In this case left is the past and right is the future and it makes a big difference whether things are continuous from the left or continuous from the right.

Right, is it true that the point is here, here, somewhere in the middle, somewhere else.

That's a serious issue.

So the next example that I want to give you is a little bit more subtle.

It's what's known as a removable discontinuity.

And so what this means is that the limit from left and right are equal.

So a picture of that would be, you have a function which is coming along like this and there's a hole maybe where, who knows either the function is undefined or maybe it's defined up here, and then it just continues on.

All right?

So the two limits are the same.

And then of course the function is begging to be redefined so that we remove that hole.

And that's why it's called a removable discontinuity.

Now let me give you an example of this, or actually a couple of examples.

So these are quite important examples which you will be working with in a few minutes.

So the first is the function g(x), which is sin x / x, and the second will be the function h(x), which is 1 - cos x over x.

So we have a problem at g(0), g(0) is undefined.

On the other hand it turns out this function has what's called a removable singularity.

Namely the limit as x goes to 0 of sin x / x does exist.

In fact it's equal to 1.

So that's a very important limit that we will work out either at the end of this lecture or the beginning of next lecture.

And similarly, the limit of 1 - cos x divided by x, as x goes to 0, is 0.

Maybe I'll put that a little farther away so you can read it.

Okay, so these are very useful facts that we're going to need later on.

And what they say is that these things have removable singularities, sorry removable discontinuity at x = 0.

All right so as I say, we'll get to that in a few minutes.

Okay so are there any questions before I move on?

Yeah?

Student: [INAUDIBLE]

Professor: The question is: why is this true?

Is that what your question is?

The answer is it's very, very unobvious, I haven't shown it to you yet, and if you were not surprised by it then that would be very strange indeed.

So we haven't done it yet.

You have to stay tuned until we do.

Okay?

We haven't shown it yet.

And actually even this other statement, which maybe seems stranger still, is also not yet explained.

Okay, so we are going to get there, as I said, either at the end of this lecture or at the beginning of next.

Other questions?

All right, so let me just continue my tour of the zoo of discontinuities.

And, I guess, I want to illustrate something with the convenience of right and left hand limits so I'll save this board about right and left-hand limits.

So a third type of discontinuity is what's known as an infinite discontinuity.

And we've already encountered one of these.

I'm going to draw them over here.

Remember the function y is 1 / x.

That's this function here.

But now I'd like to draw also the other branch of the hyperbola down here and allow myself to consider negative values of x.

So here's the graph of 1 / x.

And the convenience here of distinguishing the left and the right hand limits is very important because here I can write down that the limit as x goes to 0+ of 1 / x.

Well that's coming from the right and it's going up.

So this limit is infinity.

Whereas, the limit in the other direction, from the left, that one is going down.

And so it's quite different, it's minus infinity.

Now some people say that these limits are undefined but actually they're going in some very definite direction.

So you should, whenever possible, specify what these limits are.

On the other hand, the statement that the limit as x goes to 0 of 1 / x is infinity is simply wrong.

Okay, it's not that people don't write this.

It's just that it's wrong.

It's not that they don't write it down.

In fact you'll probably see it.

It's because people are just thinking of the right hand branch.

It's not that they're making a mistake necessarily, but anyway, it's sloppy.

And there's some sloppiness that we'll endure and others that we'll try to avoid.

So here, you want to say this, and it does make a difference.

You know, plus infinity is an infinite number of dollars and minus infinity is and infinite amount of debt.

They're actually different.

They're not the same.

So, you know, this is sloppy and this is actually more correct.

Okay, so now in addition, I just want to point out one more thing.

Remember, we calculated the derivative, and that was -1/x^2.

But, I want to draw the graph of that and make a few comments about it.

So I'm going to draw the graph directly underneath the graph of the function.

And notice what this graphs is.

It goes like this, it's always negative, and it points down.

So now this may look a little strange, that the derivative of this thing is this guy, but that's because of something very important.

And you should always remember this about derivatives.

The derivative function looks nothing like the function, necessarily.

So you should just forget about that as being an idea.

Some people feel like if one thing goes down, the other thing has to go down.

Just forget that intuition.

It's wrong.

What we're dealing with here, if you remember, is the slope.

So if you have a slope here, that corresponds to just a place over here and as the slope gets a little bit less steep, that's why we're approaching the horizontal axis.

The number is getting a little smaller as we close in.

Now over here, the slope is also negative.

It is going down and as we get down here it's getting more and more negative.

As we go here the slope, this function is going up, but its slope is going down.

All right, so the slope is down on both sides and the notation that we use for that is well suited to this left and right business.

Namely, the limit as x goes to 0 of -1 / x^2, that's going to be equal to minus infinity.

And that applies to x going to 0+ and x going to 0-.

So both have this property.

Finally let me just make one last comment about these two graphs.

This function here is an odd function and when you take the derivative of an odd function you always get an even function.

That's closely related to the fact that this 1 / x is an odd power and-- x^1 is an odd power and x^2 is an even power.

So all of this your intuition should be reinforcing the fact that these pictures look right.

Okay, now there's one last kind of discontinuity that I want to mention briefly, which I will call other ugly discontinuities.

And there are lots and lots of them.

So one example would be the function y = sin 1 / x, as x goes to 0.

And that looks a little bit like this.

Back and forth and back and forth.

It oscillates infinitely often as we tend to 0.

There's no left or right limit in this case.

So there is a very large quantity of things like that.

Fortunately we're not gonna deal with them in this course.

A lot of times in real life there are things that oscillate as time goes to infinity, but we're not going to worry about that right now.

Okay, so that's our final mention of a discontinuity, and now I need to do just one more piece of groundwork for our formulas next time.

Namely, I want to check for you one basic fact, one limiting tool.

So this is going to be a theorem.

Fortunately it's a very short theorem and has a very short proof.

So the theorem goes under the name differentiable implies continuous.

And what it says is the following: it says that if f is differentiable, in other words its-- the derivative exists at x_0, then f is continuous at x_0.

So, we're gonna need this is as a tool, it's a key step in the product and quotient rules.

So I'd like to prove it right now for you.

So here is the proof.

Fortunately the proof is just one line.

So first of all, I want to write in just the right way what it is that we have to check.

So what we have to check is that the limit, as x goes to x_0, of f(x) - f(x_0) is equal to 0.

So this is what we want to know.

We don't know it yet, but we're trying to check whether this is true or not.

So that's the same as the statement that the function is continuous because the limit of f(x) is supposed to be f(x_0) and so this difference should have limit 0.

And now, the way this is proved is just by rewriting it by multiplying and dividing by (x - x_0).

So I'll rewrite the limit as x goes to x_0 of f(x) - f(x_0) divided by x - x_0 times x - x_0.

Okay, so I wrote down the same expression that I had here.

This is just the same limit, but I multiplied and divided by (x - x_0).

And now when I take the limit what happens is the limit of the first factor is f'(x_0).

That's the thing we know exists by our assumption.

And the limit of the second factor is 0 because the limit as x goes to x_0 of (x - x_0) is clearly 0 .

So that's it.

The answer is 0, which is what we wanted.

So that's the proof.

Now there's something exceedingly fishy-looking about this proof and let me just point to it before we proceed.

Namely, you're used in limits to setting x equal to 0.

And this looks like we're multiplying, dividing by 0, exactly the thing which makes all proofs wrong in all kinds of algebraic situations and so on and so forth.

You've been taught that that never works.

Right?

But somehow these limiting tricks have found a way around this and let me just make explicit what it is.

In this limit we never are using x = x_0.

That's exactly the one value of x that we don't consider in this limit.

That's how limits are cooked up.

And that's sort of been the themes so far today, is that we don't have to consider that and so this multiplication and division by this number is legal.

It may be small, this number, but it's always non-zero.

So this really works, and it's really true, and we just checked that a differentiable function is continuous.

So I'm gonna have to carry out these limits, which are very interesting 0 / 0 limits next time.

But let's hang on for one second to see if there any questions before we stop.

Yeah, there is a question.

Student: [INAUDIBLE] Professor: Repeat this proof right here?

Just say again.

Student: [INAUDIBLE]

Professor: Okay, so there are two steps to the proof and the step that you're asking about is the first step.

Right?

And what I'm saying is if you have a number, and you multiply it by 10 / 10 it's the same number.

If you multiply it by 3 / 3 it's the same number.

2 / 2, 1 / 1, and so on.

So it is okay to change this to this, it's exactly the same thing.

That's the first step.

Yes?

Student: [INAUDIBLE]

Professor: Shhhh...

The question was how does the proof, how does this line, yeah where the question mark is.

So what I checked was that this number which is on the left hand side is equal to this very long complicated number which is equal to this number which is equal to this number.

And so I've checked that this number is equal to 0 because the last thing is 0.

This is equal to that is equal to that is equal to 0.

And that's the proof.

Yes?

Student: [INAUDIBLE]

Professor: So that's a different question.

Okay, so the hypothesis of differentiability I use because this limit is equal to this number.

That that limit exits.

That's how I use the hypothesis of the theorem.

The conclusion of the theorem is the same as this because being continuous is the same as limit as x goes to x_0 of f(x) is equal to f(x_0).

That's the definition of continuity.

And I subtracted f(x_0) from both sides to get this as being the same thing.

So this claim is continuity and it's the same as this question here.

Last question.

Student: How did you get the 0 [INAUDIBLE]

Professor: How did we get the 0 from this?

So the claim that is being made, so the claim is why is this tending to that.

So for example, I'm going to have to erase something to explain that.

So the claim is that the limit as x goes to x_0 of x - x_0 is equal to 0.

That's what I'm claiming.

Okay, does that answer your question?

Okay.

All right.

Ask me other stuff after lecture.
