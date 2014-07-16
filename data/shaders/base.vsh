attribute vec3 position;
attribute vec2 texcoord;
attribute vec3 normal;
attribute vec3 binormal;
attribute vec3 tangent;

uniform   mat4 modelView;
uniform   mat4 prjView;

varying vec2 v_tex;
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye;
varying vec3 v_tangent;
varying vec3 v_binormal;

const vec3 light_position = vec3(-30,30,0);
const vec3 eye_position   = vec3(0,0,0);

void main()
{
	vec4 p4 = vec4(position,1);
    mat4 modelMatrix = modelView;

     mat3 normalMatrix = mat3(modelMatrix[0].xyz,modelMatrix[1].xyz,modelMatrix[2].xyz);
     v_light      = normalize(light_position - position);
     v_eye        = normalize(eye_position   - position);
     v_tangent    = normalize(tangent  * normalMatrix);
     v_binormal   = normalize(binormal * normalMatrix);
     v_norm       = normalize(normal   * normalMatrix);
     mat3 tbn = mat3(v_tangent,v_binormal,v_norm);
     v_light *= tbn;
     v_eye   *= tbn;

	v_tex    = texcoord;
	
	gl_Position = p4 * modelView * prjView;
}

