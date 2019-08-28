# Simple APP

## Description
The APP exposes the following HTTP-based APIs:
* The first method:
    - The request 'PUT /hello/<username> {"dateOfBirth": "YYYY-MM-DD"}' saves/updates the given users's name and date of birth in database
    - The response is '204 No Content' or '400' for the bad requests
* The second method:
    - The request 'GET /hello/<username> {"dateOfBirth": "YYYY-MM-DD"}' returns `{"message": "Hello, <username>! Happy birthday!"` if username's birthdat is today or `{"message": "Hello, <username>! Your birthday is in N day(s)"` if username's birthday is in N days
    - The response is '200 OK' or '404' if user not found 

## Building docker image
`docker build .`

## System diagram
[draw.io](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7Vhdb9owFP01SNsDKLGTAI9Au03aJjFRrdtTZbCbeHVi5JgC%2FfWzEzsfJKysBbpJIB7s4%2Bvr%2BJzjGysdOIk3HwVaRl85JqwDHLzpwKsOAK4HQEf%2FHbzNkYHj50AoKDZBJTCjT8SAjkFXFJO0Fig5Z5Iu6%2BCCJwlZyBqGhODretg9Z%2FVVlygkDWC2QKyJ3lIsI7ML0C%2FxT4SGkV3ZDYb5SIxssNlJGiHM1xUIXnfgRHAu81a8mRCmybO85PM%2B7BktHkyQRB4y4fu30ZPrQzi7%2BTWDcxqJ4c1N12R5RGxlNrxKiUjNE8utpUGlUoyrzlhtY6nBBeMrlXm8jqgksyVaaHCtTKCwSMZM9VzVNPmJkGSz98Hdgg7lI8JjIsVWhZgJ0If5FGMhS%2Bi61MO1WFTRYmAwZCwQFplLllTDEPUXpIEGaR0QMLXqGNNH1Qx1c3Q7UzHfpxM7ppaqDDcYFnyVYIINbc%2BwytCcsClPqaQ80WIoKolQA5poqtz7ZSdAcp0BMRq2ho%2FMwJxLyWO9Fhf0iScSHVFHYGuB1dFrCgkHsCkkGJ5KSa%2BhZC7b9edZQ6B91MYUYx3TILMYqAhnT0%2B8CXW97M1RShc9TFF4lxngTmRFbJwV0KBNiL3SN8Q9xtEL6kfPC1rOntNy9oJTKeY3FZtO3z0M0m665LK75uKBiPfnFM8odk8Zm3DGRbYgvM9%2BVVzRfJXwJKuhUvAHUol2sl8xYt802aL5KxHoUaoqRCacf24jAK9uBOj7hxXhkxkhOKgIt3rjoHp8cczrHOMF%2F5pj%2Bi2O2b3mJHikL43Z%2FQalSqy22wzBjTvjDisqKV%2BJBXn%2B5iWRCIl87rLRZLnCot9CosUEYUjSx%2FrjtjFrVphyqjZS1n%2F75rWvbHdHnHybZlb18rmTyPPqidxdlXMeGokyoYttv1z7weu1Jxsqf6i20%2FNN76fumfbVptrZ2k6iHjuf5ADfAnpeVyEQWqScnfVq06dEULV9fS4z8IgeBAd6MHhLDxb3%2Fa2tDy%2F0IOjXE%2Fn%2BeT04fHMPDgew6kHnP7Gff7HfEexnS%2FdR%2FFd1X%2BHFPf5TnROayLuY6Jwman4werGJ3FeaqFLYoN%2BvFbbecNh%2F4%2BJ2qC8v79Y%2F%2B1J1y2%2BkeXj5pRle%2FwY%3D)

## Deploy APP
`kubectl create -f app-deployment.yml`
