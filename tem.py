{% extends 'allchefs/base.html' %}

{% load static%}
{% block title %}
Home
{% endblock%}

{% block content %}

<!doctype html>
<html lang="en">

<body>

    <main role="main ">
        <section class=" text-center p-5 mb-3 bg-secondary text-white">
            <div class="container ">


                <section id="cover">
                    <div id="cover-caption">
                        <div class="container">
                            <div class="row text-white">
                                <div class="col-xl-5 col-lg-6 col-md-6 col-sm-2 mx-auto text-center form p-2">

                                    <div class="px-2">
                                        <form action="" class="justify-content-center">

                                            <div class="form-group">
                                                <label class="sr-only">Email</label>
                                                <input class="form-control mr-sm-2" type="search" placeholder="Search"
                                                    aria-label="Search">
                                            </div>

                                            <button class="btn btn-outline-warning my-2 my-sm-0"
                                                type="submit">Search</button>


                                        </form>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </section>
                <!-- <form class="form-inline my-2 my-lg-0">
                                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                            </form> -->


                <h1 class="jumbotron-heading text-center p-3 mb-2 bg-secondary text-white">Welcome To The Top Chefs OF
                    The World</h1>
                <h3 class="text-light ">Pick your favorite chef</h3>
                <br>
            </div>



            <div class="album py-3 p-5 mb-5 bg-danger text-white border rounded">
                <div class="container">
                    <div class="row">
                        {% if allchefs %}
                        {% for things in allchefs %}
                        <div class="col-md-3">
                            <div class="card mb-4 box-shadow">
                                <a href="{% url 'aboutchef' things.id %}"><img
                                        class="card-img-top rounded-lg border border-primary .img-thumbnail"
                                        src="{{ things.image.url }}" alt=""></a>
                            </div>
                        </div>
                        {% endfor%}
                        {% endif%}
                    </div>
                </div>
            </div>
        </section>
    </main>
</body>

</html>